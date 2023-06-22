import sys
import shapeClass

#LOAD method. This method will take a file name as an input and output a list of Shape objects.
def LOAD(file_name):
    file = open(file_name, "r")
    multi_set = []

    print("Processing <<" + file_name + ">>...")
    #Keeping count of the number of lines, number of shapes and number of errors
    line = file.readline()
    linecount = 1
    shapecount = 0
    errorcount = 0

    #The loop will run as long as there is a next line in the file
    while line:
        test = line.split(" ")
        test[0].lower()
        #Checking the first element in the line. Helps determine what class the object generated should be
        if test[0] == "shape\n":
            shape = shapeClass.Shape()
            multi_set.append(shape)
            shapecount+=1

        elif test[0] == "circle":
            radius = float(test[1])
            #Throwing an error in case the radius is invalid
            if radius < 0:
                line_len = len(line) - 1
                print("Error: Invalid Circle on line" + str(linecount) + ":", line[:line_len])
                line = file.readline()
                linecount += 1
                errorcount+=1
                continue

            circle = shapeClass.Circle(radius)
            multi_set.append(circle)
            shapecount+=1

        elif test[0] == "ellipse":
            a = float(test[1])
            b = float(test[2])
            #Throwing an error in case the semi_major or semi_minor are not valid
            if a < 0 or b < 0:
                line_len = len(line) - 1
                print("Error: Invalid Ellipse on line " + str(linecount) + ": " + line[:line_len])
                line = file.readline()
                linecount += 1
                errorcount+=1
                continue
            ellipse = shapeClass.Ellipse(a, b)
            multi_set.append(ellipse)
            shapecount+=1

        elif test[0] == "rhombus":
            a = float(test[1])
            b = float(test[2])
            #Throwing an error in case one of the diagonals is invalid
            if a < 0 or b < 0:
                line_len = len(line) - 1
                print("Error: Invalid Rhombus on line" + str(linecount) + ":", line[:line_len])
                line = file.readline()
                linecount += 1
                errorcount+=1
                continue
            rhombus = shapeClass.Rhombus(a, b)
            multi_set.append(rhombus)
            shapecount+=1
        #In case none of the above were found, then we throw an error
        else:
            line_len = len(line) - 1
            print("Error at line: " + str(linecount) + ": " + line[:line_len])
            errorcount+=1

        line = file.readline()
        linecount+=1

    file.close()
    linecount-=1
    print("Processed " + str(linecount) + " row(s), " + str(shapecount) + " shape(s) added, " + str(errorcount) + " error(s)")
    shapeClass.id_g = 1
    return multi_set

#Method that will print the count of each type of shape
def SUMMARY(multi_set):
    circle_count = 0
    ellipse_count = 0
    rhombus_count = 0
    shape_count = 0

    #Loop that goes through the multi_set and increments the count for each type of shape
    for x in multi_set:
        if type(x).__name__ == "Circle":
            circle_count+=1
            shape_count+=1
        elif type(x).__name__ == "Ellipse":
            ellipse_count+=1
            shape_count += 1
        elif type(x).__name__ == "Rhombus":
            rhombus_count+=1
            shape_count += 1
        elif type(x).__name__ == "Shape":
            shape_count+=1

    print("Circle(s): " + str(circle_count))
    print("Ellipse(s): " + str(ellipse_count))
    print("Rhombus(es): " + str(rhombus_count))
    print("Shape(s): " + str(shape_count))

    return

#Method that returns what will be printed into a file if we call the method SAVE. This method will print into the
#standard output
def DETAILS(multi_set):

    #Checks what type of shape each element is and prints accordingly
    for x in multi_set:
        if type(x).__name__ == "Shape":
            print("shape")

    for x in multi_set:
        if type(x).__name__ == "Circle":
            print("circle " + str(int(x.radius)))

    for x in multi_set:
        if type(x).__name__ == "Ellipse":
            print("ellipse " + str(int(x.semi_minor)) + " " +  str(int(x.semi_major)))

    for x in multi_set:
        if type(x).__name__ == "Rhombus":
            print("rhombus " + str(int(x.first_diagonal)) + " " +  str(int(x.second_diagonal)))

    return


#Method that goes through the multi set and calls the print method for each object
def PRINT(multi_set):
    for x in multi_set:
        x.print()
    return

#Method that exits the program
def QUIT():
    print()
    print("The program is going to terminate")
    sys.exit(0)

#Method that will save the current contents inside the multi set inside a file that is specified by the user
def SAVE(multi_set, filename):
    file = open(filename, "w")

    # Checks what type of shape each element is and prints accordingly
    for x in multi_set:
        if type(x).__name__ == "Shape":
            file.write("shape\n")

    for x in multi_set:
        if type(x).__name__ == "Circle":
            file.write("circle " + str(int(x.radius)) + "\n")

    for x in multi_set:
        if type(x).__name__ == "Ellipse":
            file.write("ellipse " + str(int(x.semi_minor)) + " " +  str(int(x.semi_major)) + "\n")

    for x in multi_set:
        if type(x).__name__ == "Rhombus":
            file.write("rhombus " + str(int(x.first_diagonal)) + " " +  str(int(x.second_diagonal)) + "\n")


    return

#Goes through the list and transforms it into a set that is then returned
def TOSET(multiset):
    #Creating lists that will keep track of the elements that have been added inside the set
    ellipse_list = []
    circle_list = []
    rhombus_list = []
    the_set = set()
    shape_count = 0

    for x in multiset:
        #Only one shape element will be allowed in the set
        if type(x).__name__ == "Shape":
            if shape_count > 0:
                continue
            the_set.add(x)
            shape_count+=1

        elif type(x).__name__ == "Circle":
            circle_count = 0
            #Comparing the current element to each element in circle_list until we find 2 elements that are equal
            for y in circle_list:
                if x.radius == y.radius:
                    circle_count+=1
                    break

            #If we found that the current element is the same as one stored in circle_list we check the next element
            #in the multi set
            if circle_count > 0:
                continue

            #Otherwise we add the current element into the set and into the circle_list
            the_set.add(x)
            circle_list.append(x)

        elif type(x).__name__ == "Ellipse":
            ellipse_count = 0

            # Comparing the current element to each element in ellipse_list until we find 2 elements that are equal
            for y in ellipse_list:
                if x.semi_major == y.semi_major and x.semi_minor == y.semi_minor:
                    ellipse_count+=1
                    break

            # If we found that the current element is the same as one stored in ellipse_list we check the next element
            # in the multi set
            if ellipse_count > 0:
                continue

            # Otherwise we add the current element into the set and into the ellipse_list
            the_set.add(x)
            ellipse_list.append(x)

        elif type(x).__name__ == "Rhombus":
            rhombus_count = 0

            # Comparing the current element to each element in rhombus_list until we find 2 elements that are equal
            for y in rhombus_list:
                if x.first_diagonal == y.first_diagonal and x.second_diagonal == y.second_diagonal:
                    rhombus_count+=1
                    break

            # If we found that the current element is the same as one stored in rhombus_list we check the next element
            # in the multi set
            if rhombus_count > 0:
                continue

            # Otherwise we add the current element into the set and into the rhombus_list
            the_set.add(x)
            rhombus_list.append(x)

    return the_set

#Method that will print all of the commands and what they do to the user. This is only used in order to remind the user
#of the commands that they can use
def HELP():
    print("LOAD 'file': loads a database of shapes. Takes the filepath as an input.")
    print("TOSET: converts the current multi-set in memory to a set (removes duplicates).")
    print("SAVE 'file': saves the current in-memory database to a file which is the input.")
    print("PRINT: prints the current in-memory database to the standard output.")
    print("SUMMARY: prints the summary of the in-memory database to the standard output.")
    print("DETAILS: prints the detailed information of the in-memory database objects to the standard output.")
    print("QUIT: terminate the program.")
    print("HELP: prints this menu if you need a reminder.")
    return