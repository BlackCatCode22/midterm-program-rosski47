import os
import numpy as np
import math
import re


def birthday_calc(season,age):
    # year counts from 2022 because these dates have not yet occurred in 2023
    year = 2022 - int(age.strip())
        # spring = "March 21"
        # summer = "June 21"
        # fall = "September 21"
        # winter = "December 21"
        # else = "July 21"
    if season.endswith("spring"):
        date = "March 21"
    elif season.endswith("summer"):
        date = "June 21"
    elif season.endswith("fall"):
        date = "September 21"
    elif season.endswith("winter"):
        date = "December 21"
    else:
        date = "July 21"
    birthday = date + ", " + str(year)
    return birthday

def lastWord(string):

    # split by space and converting
    # string to list and
    lis = list(string.split(" "))

    # length of list
    length = len(lis)

    # returning last element in list
    return lis[length - 1]

# uniqueID function adapted from approved solution file
def uniqueID(species, species_count):
    match species:
        case "hyena":
            prefix = "HY"
        case "lion":
            prefix = "LI"
        case "tiger":
            prefix = "TI"
        case "bear":
            prefix = "BE"
        case default:
            prefix = "XX"

    return prefix + "_0" + str(species_count)

def LineCountList(lines):
    line_count = 0
    list_of_lines = []
    for line in lines:
        print("Line " + str(line_count+1) + ":  " + line)
        line_count += 1
        list_of_lines.append(line)
    return list_of_lines


name_file = open("animalNames.txt", "r", encoding="utf-8")
name_lines = name_file.readlines()
name_file.close()

name_lines_list = LineCountList(name_lines)
# Demonstrate the list
print("\n\n Here is a list of the lines in the animal names file...\n\n")
print("line 0 is: " + str(name_lines_list[0]))

hyena_names_list = name_lines_list[2].replace(',',"").split()
lion_names_list = name_lines_list[6].replace(',',"").split()
bears_names_list = name_lines_list[10].replace(',',"").split()
tigers_names_list = name_lines_list[14].replace(',',"").split()

print(hyena_names_list)
print(lion_names_list)
print(bears_names_list)
print(tigers_names_list)


# Global variables needed for some user-defined functions
num_of_hyenas = 0
num_of_lions = 0
num_of_tigers = 0
num_of_bears = 0

# Global lists needed for organizing animals into a single-species habitats
hyenas = []
lions = []
tigers = []
bears = []
#oh my!

animal_file = open("arrivingAnimals.txt", "r", encoding="utf-8")
animal_lines = animal_file.readlines()
animal_file.close()

animal_lines_list = LineCountList(animal_lines)
print(animal_lines_list)

# Get the file contents into an array
# Talk about the difference between list and array
my_array = np.asarray(animal_lines_list)

# Find how many elements are in our new array
num_of_array_elements = my_array.size
print("Array Elements: " + str(num_of_array_elements))
print(my_array)
# Output the new array
array_line = 0
for element in my_array:

    # get the data elements needed from this one line for the birthday (Method adapted from approved solution file)
    ########################## Split on blank space to get words in the line
    split_on_space = my_array[array_line].split(" ")
    print(split_on_space)



    years_old = split_on_space[0]


    print("years_old: " + years_old)


    sex = split_on_space[3]
    print("sex: " + sex)


    species = split_on_space[4]
    print("species: " + species)


    species = re.sub(",", "", species)

    # test with a print()
    print(" species without a comma: " + species)

    # season of birth
    season = split_on_space[7]
    print("season: " + season)

    # we have a comma at the end of this word, so we must remove it
    season = re.sub(",", "", season)

    # test with a print()
    print(" season without a comma: " + season)

    # we got a couple of our needed data elements. now let's calculate what we can using the functions we wrote
    birth_date = birthday_calc(season, years_old)
    print("birthdate: " + birth_date)

    if (species == "hyena"):
        num_of_hyenas += 1

        # and now we can call uniqueID()
        unique_id = uniqueID(species, num_of_hyenas)
        print("Number of Hyenas: " + str(num_of_hyenas))
        # get a name from the name list that we created with file io
        # if we are here, we know we need a hyena name
        name = hyena_names_list[num_of_hyenas]
    elif (species == "lion"):
        num_of_lions += 1

        # and now we can call uniqueID()
        unique_id = uniqueID(species, num_of_lions)

        # get a name from the name list that we created with file io
        # if we are here, we know we need a lion name
        name = lion_names_list[num_of_lions]
    elif (species == "tiger"):
        num_of_tigers += 1

        # and now we can call uniqueID()
        unique_id = uniqueID(species, num_of_tigers)

        # get a name from the name list that we created with file io
        # if we are here, we know we need a hyena name
        name = tigers_names_list[num_of_tigers]
    elif (species == "bear"):
        num_of_bears += 1

        # and now we can call uniqueID()
        unique_id = uniqueID(species, num_of_bears)

        # get a name from the name list that we created with file io
        # if we are here, we know we need a hyena name
        name = bears_names_list[num_of_bears]
    else:
        print("\n error in incrementing species")

    print("unique_id: " + unique_id)
    print("name is: " + name)
    ##########################################

    # Split on comma because some data elements (like color, wright, and origin)
    # have a varied number of words
    after_split_on_comma = my_array[array_line].split(", ")

    print(after_split_on_comma)

    color = after_split_on_comma[2]
    color = re.sub(" color", "", color)
    print("color = " + color)

    weight = after_split_on_comma[3]
    print("weight is: " + weight)

    origin = after_split_on_comma[4] + ", " + after_split_on_comma[5]
    origin = re.sub("from ", "", origin)
    print("origin = " + origin)

    # desperately trying to get rid of the lf+cr that is showing up in the output file...
    origin = origin.strip()

    # arrival date = due date of March 19, 2023
    arrival_date = "March 19, 2023"

    # Create output strings
    str01 = unique_id + "; " + name + "; " + str(
        years_old) + " years old; " + "Birthdate: " + birth_date + "; "
    str02 = "Color: " + color.title() + "; Sex: " + sex.title() + "; Weight: " + weight.title() + "; Origin: " + origin\
            + "; Arrived: " + arrival_date

    output_line = str01 + str02

    print("\noutput_line = " + output_line)

    # get this output line into the proper list()
    if (species == "hyena"):
        hyenas.append(output_line)
    elif (species == "tiger"):
        tigers.append(output_line)
    elif (species == "lion"):
        lions.append(output_line)
    else:
        bears.append(output_line)

    array_line += 1
    ############################################### End of processing each line with the two splits()

    print("Hyena Habitat: \n\n")
    for line in hyenas:
        print(line + "\n")

    my_file = open("midTermOutput.txt", "w", encoding="utf-8")

    my_file.write("Midterm Program Output; by Ross Williams, Spring 2023, Fresno, CA\n\n")

    my_file.write("Hyena Habitat: \n\n")
    for i in hyenas:
        my_file.write(i)
        my_file.write("\n")
    my_file.write("\n\n")

    my_file.write("Lion Habitat: \n\n")
    for i in lions:
        my_file.write(i)
        my_file.write("\n")
    my_file.write("\n\n")

    my_file.write("Tiger Habitat: \n\n")
    for i in tigers:
        my_file.write(i)
        my_file.write("\n")
    my_file.write("\n\n")

    my_file.write("Bear Habitat: \n\n")
    for i in bears:
        my_file.write(i)
        my_file.write("\n")
    my_file.write("\n\n")

    # if you open a barn door, make sure you close it.
    my_file.close()
