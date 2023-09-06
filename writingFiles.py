

answer = input("Would you like to add to file (a), restore file (w), or see file (r)?: ")
print()

#############################################################
# APPENDING
if(answer.lower() == "a"):

    # Reminder: "a" appends to the end, while "w" fully overwrites the file
    employee_file = open("supportFiles/employees.txt", "a")

    answer = input("Enter name: ")
    job = input("Enter job: ")

    #write() lets us append a line to the end of the file
    #BE CAREFUL, as writing could mess up a file!
    # when appending, you have to add a new line to the start of the edit for a new line
    employee_file.write("\n" + answer + " - " + job)

    print()
    employee_file.close()

##############################################################
# WRITING
elif(answer.lower() == "w"):

    #"w" lets us fully overwrite the file
    employee_file = open("supportFiles/employees.txt", "w")

    employee_file.write("Jim -  Salesman\nDwight - Salesman\nPam - Receptionist\nMichael - Manager\nOscar - Accountant")

    employee_file.close()

elif(answer.lower() == "r"):
    employee_file = open("supportFiles/employees.txt", "r")

    print(employee_file.read())

    print()
    employee_file.close()

else:
    print("Not a valid input")
    print()

##########################################################################3
# CREATING NEW FILE
answer = input("Would you like to create a new file?: ")

if(answer.lower() == "y" or answer.lower() == "yes"):

    # Typing in an unknown file with "w" and an extension creates a file instead
    new_file = open("supportFiles/newFile.html", "w")

    new_file.write("<p>This is HTML</p>")

    print()
    new_file.close()

else:
    print()

