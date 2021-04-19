-- /* Triggers */

-- CREATE TRIGGER IngPres
-- BEFORE INSERT ON orders
-- FOR EACH ROW
-- BEGIN
-- 	IF NEW.filled is NULL THEN
-- 		RETURN NEW;
-- 	END IF;
-- 	RETURN NULL;
-- END;

-- CREATE TRIGGER RecAmtTrig
-- BEFORE insert ON orders
-- FOR EACH ROW
-- DECLARE 
-- 	I RECORD;
-- BEGIN
-- 	FOR I IN

-- 		SELECT 
-- 			recipe_ingredient.amount AS recamt, inventory.amount AS invamt 
-- 		FROM 
-- 			recipe_ingredient JOIN inventory ON recipe_ingredient.ingredient = inventory.ingredient 
-- 		WHERE 
-- 			recipe_ingredient.recipe = NEW.recipe
--     LOOP
-- 		IF I.recamt * NEW.quantity > I.invamt THEN
-- 			RETURN NULL;
-- 		END IF;
-- 	END LOOP;
-- 	RETURN NEW;
-- END;

-- /* Below is a trigger we are fire after insert in the order table to update the corresponding inventory */

-- CREATE TRIGGER InvTrig
-- BEFORE UPDATE ON orders
-- FOR EACH ROW 
-- DECLARE 
-- 	J RECORD;
-- BEGIN
-- 	FOR J IN

-- 		SELECT
-- 			inventory.ingredient AS inving, recipe_ingredient.amount AS recamt, inventory.amount AS invamt 
-- 		FROM
-- 			recipe_ingredient JOIN inventory ON inventory.ingredient = recipe_ingredient.ingredient
-- 		WHERE
-- 			recipe_ingredient.recipe = NEW.recipe
--     LOOP
-- 		UPDATE inventory SET amount = J.invamt - NEW.quantity * J.recamt  WHERE ingredient = J.inving;
-- 	END LOOP;	
-- 	RETURN NEW;
-- END;

-- /* Here is a trigger to make column immutable after update from null value*/

-- CREATE TRIGGER filledColTrig
-- BEFORE UPDATE ON orders
-- FOR EACH ROW
-- BEGIN
-- 	IF OLD.filled IS NULL THEN
-- 		RETURN NEW;
-- 	END IF;
-- RETURN NULL;
-- END;
-- $filledCol$ 
-- LANGUAGE plpgsql;


/* Functions */

CREATE FUNCTION CheckFillFunc() RETURNS trigger AS $checkfun$
BEGIN
	IF NEW.filled is NULL THEN
		RETURN NEW;
	END IF;
	RETURN NULL;
END;
$checkfun$ 
LANGUAGE plpgsql;
  
CREATE FUNCTION RecAmt() RETURNS trigger AS $RecAmt$
DECLARE 
	ROW RECORD;
BEGIN
	FOR ROW IN

		SELECT 
			recipe_ingredient.amount AS recamt, inventory.amount AS invamt 
		FROM 
			recipe_ingredient JOIN inventory ON recipe_ingredient.ingredient = inventory.ingredient 
		WHERE 
			recipe_ingredient.recipe = NEW.recipe
    LOOP
		IF ROW.recamt * NEW.quantity > ROW.invamt THEN
			RETURN NULL;
		END IF;
	END LOOP;
	RETURN NEW;
END;
$RecAmt$ 
LANGUAGE plpgsql;	

CREATE FUNCTION InvTrigger() RETURNS trigger AS $InvTrigger$
DECLARE 
	ROW RECORD;
BEGIN
	FOR ROW IN

		SELECT
			inventory.ingredient AS inving, recipe_ingredient.amount AS recamt, inventory.amount AS invamt 
		FROM
			recipe_ingredient JOIN inventory ON inventory.ingredient = recipe_ingredient.ingredient
		WHERE
			recipe_ingredient.recipe = NEW.recipe
    LOOP
		UPDATE inventory SET amount = ROW.invamt - NEW.quantity * ROW.recamt  WHERE ingredient = ROW.inving;
	END LOOP;	
	RETURN NEW;
END;
$InvTrigger$ 
LANGUAGE plpgsql;	

CREATE FUNCTION filledCol() RETURNS trigger AS $filledCol$
BEGIN
	IF OLD.filled IS NULL THEN
		RETURN NEW;
	END IF;
	RETURN NULL;
END;
$filledCol$ 
LANGUAGE plpgsql;

/* Triggers */

CREATE TRIGGER IngPres
BEFORE INSERT ON orders
FOR EACH ROW EXECUTE PROCEDURE CheckFillFunc();

CREATE TRIGGER RecAmtTrig
BEFORE insert ON orders
FOR EACH ROW EXECUTE PROCEDURE RecAmt();

/* Below is a trigger we are fire after insert in the order table to update the corresponding inventory */

CREATE TRIGGER InvTrig
BEFORE UPDATE ON orders
FOR EACH ROW EXECUTE PROCEDURE InvTrigger();

/* Here is a trigger to make column immutable after update from null value*/

CREATE TRIGGER filledColTrig
BEFORE UPDATE ON orders
FOR EACH ROW EXECUTE PROCEDURE filledCol();