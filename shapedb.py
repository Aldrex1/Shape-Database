import sys
import operations

def main():

    multi_set = []

    #Checking if when the program is loaded from the terminal if it has any arguments. If it has, the argument has to
    #be load. This is because otherwise we don't have any elements in the database. Thus, if it's something other than
    #LOAD we return an error and then print all the commands the user can use
    if sys.argv.__len__() > 1:
        if sys.argv[1] == "LOAD":
            multi_set = operations.LOAD(sys.argv[2])
        else:
            print("ERROR: no data has been loaded in the database. Please use LOAD before using other commands.")

    #These commands are printed whether or not the user makes the error of not loading a database
    print("Welcome! These are the following commands that you can use in this program:")
    print()
    operations.HELP()

    #This loop will go on forever until QUIT() is called
    while True:
        #Taking input from the user
        consoleIn = input("\n>>")
        command_string = consoleIn.split()

        command_string[0] = command_string[0].upper()

        #These are the commands that can be done when the database is empty
        if command_string[0] == "LOAD":
            multi_set = operations.LOAD(command_string[1])
        elif command_string[0] == "QUIT":
            operations.QUIT()
        elif command_string[0] == "HELP":
            operations.HELP()

        #This checks if the database is empty. If it is then we prompt the user for another command again
        if not (bool(multi_set)):
            print("No database has been loaded. Please try again by using the LOAD command followed of a file name.")
            continue

        #These are the functions we can call once we have a loaded database
        if command_string[0] == "TOSET":
            multi_set = operations.TOSET(multi_set)
        elif command_string[0] == "SAVE":
            operations.SAVE(multi_set,command_string[1])
        elif command_string[0] == "PRINT":
            operations.PRINT(multi_set)
        elif command_string[0] == "SUMMARY":
            operations.SUMMARY(multi_set)
        elif command_string[0] == "DETAILS":
            operations.DETAILS(multi_set)


#Calling the main method if the shapedb.py is the main file
if __name__ == "__main__":
    main()