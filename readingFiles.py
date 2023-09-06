# Lets us read a txt file

# open() lets us open a file from a certain location. Here, employees.txt is in the folder supportFiles
#   "r" lets us only read a file. "w" lets us write and edit it. "a" lets us append info to the end of the file.
#   "r+" lets us both read and write to a file

# Make sure to store the opened file in a variable
employee_file = open("supportFiles/employees.txt", "r")

# readable is a boolean value that checks if we can read the file
print(employee_file.readable())                         #returns True
print()

# print(employee_file.read())                             # Reads the entire file
# print(employee_file.readline())                         # Reads the current line the file is on (like a pointer) & moves pointer to next
# print(employee_file.readlines())                        # Takes each line of the file & puts it in a list
# print(employee_file.readlines()[1])                     # Puts the second line of the file in an array

for employee in employee_file.readlines():              # Lets us print or do something to each line in a for loop
    print(employee)

# Remember to close the file to prevent any errors
employee_file.close()

print()
