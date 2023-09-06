# Lists are for large amounts of data
# List - Structure in Python that can store information

friends = ["Kevin", "Karen", "Gym", "Jim"]

print(friends)              # Entire list
print(friends[0])           # Kevin
print(friends[3])           # Jim
print(friends[-2])          # Gym
        # negative numbers start from the back of the list
print(friends[1:])          # Grabs position 1 & all names after that
print(friends[0:2])         # Grabs positions from 0 to 2

friends[1] = "Mike"
print(friends[1])           # Mike
