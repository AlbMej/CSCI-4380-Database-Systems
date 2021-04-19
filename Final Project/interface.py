from blessings import Terminal
import queries
from ascii_art import *
"""
A clean CLI for our Spring 2019 Database Systems Project. 
"""

class UserInterface:
    """
    TODO: Fix styling. There is a lack of line breaks and spacing.
    """
    @staticmethod
    def displayOptions(t):
        """
        For Main Menu
        """
        print(t.bold('Choose one of the following options:'))
        print(t.bold('    (1) Relationship between type of liquor licenses and violent crime ratio'))
        print(t.bold('    (2) Crimes per liquor license'))
        print(t.bold('    (3) View Liquor Agency Responsibility'))
        print(t.bold('    (4) Number of liquor stores per county'))
        print(t.bold('    (5) Change in crime over the years'))
        print(t.bold('    (6) Percentage of violent crime for type of liquor license'))
        print(t.bold('    Enter q to quit'))

    @staticmethod
    def displayViolentOptions(t):
        """
        For TypeRationQuery
        """
        print(t.bold_underline("LICENSE TYPE SELECT"))
        print(t.bold('What type of license do you want to see?'))
        print(t.bold('    (1) Bar License'))
        print(t.bold('    (2) Restaurant License'))
        print(t.bold('    (3) Store License'))
        print(t.bold('    (4) Alcohol Maker License'))
        print(t.bold('    (5) Other Licenses'))
        print(t.bold('    Enter q to quit'))

    @staticmethod
    def displayCrimeLiquorOptions(t):
        """
        For CrimeLiquor Query
        """
        print(t.bold_underline("CRIME LIQUOR SELECT"))
        print(t.bold('What would you like to see'))
        print(t.bold('    (1) Data on all counties'))
        print(t.bold('    (2) Lowest number of crimes per liquor license'))
        print(t.bold('    (3) Highest number of crimes per liquor license'))
        print(t.bold('    Enter q to quit'))

    @staticmethod
    def displayCrimeOptions(t):
        """
        For CrimeChangeQuery
        """
        print(t.bold_underline("CRIME TYPE SELECT"))
        print(t.bold('What type of crime do you want to see?'))
        print(t.bold('    (1) All'))
        print(t.bold('    (2) All Violent'))
        print(t.bold('    (3) Rape'))
        print(t.bold('    (4) Larceny'))
        print(t.bold('    (5) Property Crimes'))
        print(t.bold('    Enter q to quit'))

    @staticmethod
    def displayLiquorCrimeType(t):
        """
        For LiquorCrimeTypeQuery
        """
        print(t.bold_underline("LIQUOR TYPE TO CRIME SELECT"))
        print(t.bold('What type of crime do you want to see?'))
        print(t.bold('    (1) Rape'))
        print(t.bold('    (2) Murder'))
        print(t.bold('    (3) Aggravated Assault'))
        print(t.bold('    (4) Robbery'))
        print(t.bold('    Enter q to quit'))

    # @staticmethod
    # def displayLicenseTypeOptions(t):
    #     print(t.bold)

    @staticmethod
    def TypeRatioQuery(t):
        """
        Option 1 from Main Menu
        """
        UserInterface.displayViolentOptions(t)
        userChoice = input()
        while userChoice != 'q':
            if userChoice == "q": break
            elif userChoice == '1' or userChoice == '2' or userChoice == '3' or userChoice == '4' or userChoice == '5' :
                print("-----------------------------------------------------------")
                conn = queries.getConn()
                queries.typeRatioToCrimeRatio(int(userChoice), conn)
                print("-----------------------------------------------------------")
            else:
                print(t.bold_red("Invalid input. Please type in a number 1-5"))
            UserInterface.displayViolentOptions(t)
            userChoice = input()
        print()
        print(t.bold_magenta("Exited Option 1"))
        print()

    @staticmethod
    def CrimeLiquorQuery(t):
        """
        Option 2 from Main Menu
        """
        UserInterface.displayCrimeLiquorOptions(t)
        userChoice = input()
        conn = queries.getConn()
        while userChoice != 'q':
            if userChoice == "q":
                break
            elif userChoice == '1':
                print("-----------------------------------------------------------")
                print("Loading...")
                print()
                queries.counties_liq_crime(1, conn)
                print("-----------------------------------------------------------")
            elif userChoice == '2':
                print("-----------------------------------------------------------")
                print("Loading...")
                print()
                queries.counties_liq_crime(2, conn)
                print("-----------------------------------------------------------")
            elif userChoice == '3':
                print("-----------------------------------------------------------")
                print("Loading...")
                print()
                queries.counties_liq_crime(3, conn)
                print("-----------------------------------------------------------")
            else:
                print(t.bold_red("Invalid input. Please type in a number from 1-6"))
            UserInterface.displayCrimeLiquorOptions(t)
            userChoice = input()
        print()
        print(t.bold_cyan("Exited Option 2"))
        print()

    @staticmethod
    def CrimeChangeQuery(t):
        """
        Option 5 from Main Menu
        """
        UserInterface.displayCrimeOptions(t)
        userChoice = input()
        while userChoice != 'q':
            if userChoice == "q": break
            elif userChoice == '1' or userChoice == '2' or userChoice == '3' or userChoice == '4' or userChoice == '5' :
                print(t.bold('How many years ago do you want to compare to? (Max 27)'))
                yearsBack = input()

                while not yearsBack.isdigit(): 
                    print()
                    print(t.bold_red('Not a valid integer.'))
                    print(t.bold('How many years ago do you want to compare to? (Max 27)'))
                    yearsBack = input()
                    print()
                    
                while int(yearsBack) > 27 or int(yearsBack) <=0:
                    print()
                    print(t.bold_red('Integer out of range. Please select a number from 0-27'))
                    print(t.bold('How many years ago do you want to compare to? (Max 27)'))
                    yearsBack = input()
                    print()
                
                print(t.bold('What county do you want to look at? type "all" to look at all of them'))
                county = input().lower()
                conn = queries.getConn()
                print("-----------------------------------------------------------")
                queries.crimeChange(int(userChoice), int(yearsBack), county, conn)
                print("-----------------------------------------------------------")
            else:
                print(t.bold_red("Invalid input. Please type in a number from 1-5"))
            UserInterface.displayCrimeOptions(t)
            userChoice = input()
        print()
        print(t.bold_green("Exited Option 5"))
        print()

    @staticmethod
    def LiquorCrimeTypeQuery(t):
        """
        Option 6 from Main Menu
        """
        UserInterface.displayLiquorCrimeType(t)
        userChoice = input()
        conn = queries.getConn()
        while userChoice != 'q':
            if userChoice == "q": break
            elif userChoice == '1':
                print("-----------------------------------------------------------")
                print("Loading...")
                print()
                queries.liquor_crimes('rape', conn)
                print("-----------------------------------------------------------")
            elif userChoice == '2':
                print("-----------------------------------------------------------")
                print("Loading...")
                print()
                queries.liquor_crimes('murder', conn)
                print("-----------------------------------------------------------")
            elif userChoice == '3':
                print("-----------------------------------------------------------")
                print("Loading...")
                print()
                queries.liquor_crimes('aggravated', conn)
                print("-----------------------------------------------------------")
            elif userChoice == '4':
                print("-----------------------------------------------------------")
                print("Loading...")
                print()
                queries.liquor_crimes('robbery', conn)
                print("-----------------------------------------------------------")
            else:
                print(t.bold_red("Invalid input. Please type in a number from 1-6"))
            UserInterface.displayLiquorCrimeType(t)
            userChoice = input()
        print()
        print(t.bold_cyan("Exited Option 6"))
        print()

    @staticmethod
    def MainMenu():
        t = Terminal()
        MainMenuTitle = t.red_on_green('MAIN MENU')
        print(MainMenuTitle)
        UserInterface.displayOptions(t)
        conn = queries.getConn()

        userChoice = input()
        while userChoice != 'q':
            if userChoice == "q":
                break
            elif userChoice == '1':
                print()
                UserInterface.TypeRatioQuery(t)
                print(MainMenuTitle)
            elif userChoice == '2':
                UserInterface.CrimeLiquorQuery(t)
                print(MainMenuTitle)
            elif userChoice == '3':
                print("-----------------------------------------------------------")
                print("Loading...")
                print()
                queries.responsibleratio(conn)
                print("-----------------------------------------------------------")
                print(MainMenuTitle)
            elif userChoice == '4':
                print("-----------------------------------------------------------")
                queries.liquorstores(conn)
                print("-----------------------------------------------------------")
                print(MainMenuTitle)
            elif userChoice == '5':
                UserInterface.CrimeChangeQuery(t)
                print(MainMenuTitle)
            elif userChoice == '6':
                UserInterface.LiquorCrimeTypeQuery(t)
                print(MainMenuTitle)
            # elif userChoice == '7':
            #     print(Terminal().bold_red(sisMan()))
            else:
                print(t.bold_red("Invalid input. Please type in a number from 1-6"))
            UserInterface.displayOptions(t)
            userChoice = input()
        print()
        print(t.bold_blue("EXITED APPLICATION"))
        print()

if __name__ == '__main__':
    print(Terminal().bold_yellow(dbs_title()))
    UserInterface.MainMenu()
