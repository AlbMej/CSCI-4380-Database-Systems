import psycopg2
import psycopg2.extras
from data_structures import RecipeInstructions
import pprint

class RestaurantData:

    def __init__(self, connection_string):
        self.conn = psycopg2.connect(connection_string)

    def check_connectivity(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM recipe LIMIT 1")
        records = cursor.fetchall()
        return len(records) == 1

    def find_recipe(self, recipe_name):
        """
        This accepts a string containing a partial or full recipe name, 
        perform a case-insensitive search of the recipe table, and returns a 
        list of dict objects (or dict-like objects) representing the recipes found. 
        The list of dictionaries should be in the form {'name': name_of_recipe} .
        Note that this does not include any search for ingredients.
        """
        cur = self.conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
        cur.execute("SELECT recipe.name FROM recipe")
        res = cur.fetchall()    

        recipeNameDicts = []
        for recipeDict in res:
            if recipe_name in recipeDict['name'].lower(): 
                recipeNameDicts.append(recipeDict)
        return recipeNameDicts

    def get_recipe_instructions(self, recipe_name):
        """
        This accepts a string containing an exact recipe name. 
        (The recipe name is the key to the recipe table, so the exact match 
        guarantees at most one recipe.) It returns a populated RecipeInstructions object.
        """
        cur = self.conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
        sqlQuery = """
        SELECT 
            recipe.name, recipe.instructions, ingredient.name AS ingredientName, recipe_ingredient.ingredient, recipe_ingredient.recipe, recipe_ingredient.amount
        FROM
            recipe 
            INNER JOIN recipe_ingredient 
            ON recipe_ingredient.recipe = recipe.name
            INNER JOIN ingredient 
            ON ingredient.code = recipe_ingredient.ingredient
        WHERE 
            recipe.name = %s
        """

        cur.execute(sqlQuery, (recipe_name,))
        res = cur.fetchall() 

        recipeInstructions = RecipeInstructions(recipe_name, None, [])
        ingredientsForRecipe = []
        
        for recipeDict in res:
            instructions = recipeDict['instructions']
            ingName, ingAmt = recipeDict['ingredientname'], recipeDict['amount']
            ingredientsForRecipe.append((ingName, ingAmt))

        instructions = res[0]['instructions']
        recipeInstructions = RecipeInstructions(recipe_name, instructions, ingredientsForRecipe)
        return recipeInstructions

        

    def get_seasonal_menu(self, season):
        """
        This accepts a string containing an exact season name. It returns a list 
        of tuples of the form (recipeName, isKosher), using the definition that a recipe is kosher 
        if all of its ingredients are kosher. Note that there is a "meta-season:" All, whose recipes 
        should appear on the menu, regardless of the season.
        """
        cur = self.conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
        sqlQuery = """
        SELECT 
            ingredient.name AS ingredientName, ingredient.is_kosher, recipe_ingredient.ingredient AS code, recipe_ingredient.recipe
        FROM
            recipe 
            INNER JOIN recipe_ingredient 
            ON recipe_ingredient.recipe = recipe.name
            INNER JOIN ingredient 
            ON ingredient.code = recipe_ingredient.ingredient
        WHERE 
            recipe.season = %s OR recipe.season = 'All'
        """

        cur.execute(sqlQuery, (season,))
        res = cur.fetchall() 
        
        seasonRecipes = [] #(recipeName, isKosher) 
        recipeIngredients = {}
        
        for recipeDict in res:
            ingredientsForRecipe = [] 
            recipeName = recipeDict['recipe']
            ingName, ingIsKosher= recipeDict['ingredientname'], recipeDict['is_kosher']
            #ingredientForRecipe = [(ingName, ingIsKosher)]
            curIngIsKosher = [(ingIsKosher)]
            recipeIngredients[recipeName] = recipeIngredients.get(recipeName, []) + curIngIsKosher

        for recipe in recipeIngredients:
            isAllKosher = all(recipeIngredients[recipe])
            seasonRecipes.append((recipe,isAllKosher))

        return seasonRecipes

    def update_ingredient_price(self, ingredient_code, price):
        """
        This updates the price of the ingredient with the new price. 
        It returns the number of rows updated.
        """
        cur = self.conn.cursor()
        sqlQuery = """ 
        UPDATE ingredient 
        SET cost_per_unit = %s
        WHERE code = %s
        """ 
        cur.execute(sqlQuery, (price, ingredient_code))
        self.conn.commit()
        rowsUpdated = cur.rowcount 
        return rowsUpdated

    def add_new_recipe(self, recipe_instructions, servings, course, season):
        """
        This accepts a RecipeInstruction object, as well as values for servings, course, 
        and season for the new recipe. It returns True if the recipe was successfully inserted, 
        and False if it was not. Note that if the recipe includes an ingredient that does not
        exist in the ingredient table, the insert should fail.
        """
        
        cur = self.conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
        recipeName, ingredients = recipe_instructions.name, recipe_instructions.ingredients
        checkIngQuery = "SELECT code FROM ingredient WHERE name = %s"
        recipeInsertQuery = "INSERT INTO recipe VALUES (%s, %s, %s, %s, %s )"
        recipeIngInsertQuery = "INSERT INTO recipe_ingredient VALUES (%s, %s, %s)"
         
        recipeIngs = []

        for ingName, ingAmt in ingredients:
            cur.execute(checkIngQuery, (ingName, ))
            res = cur.fetchall()
            if not res:
                #raise ValueError('Ingredient does not exist in ingredient table!')
                return False 
            ingCode = res[0]['code']
            recipeIngs.append((ingCode, recipeName, ingAmt))

        cur.execute(recipeInsertQuery, (recipeName, ingredients, servings, course, season))
        cur.executemany(recipeIngInsertQuery, recipeIngs)
        self.conn.commit()
        return True
