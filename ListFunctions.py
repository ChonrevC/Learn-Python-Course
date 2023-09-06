# List also lets us organize the data inside

numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

print(friends)                  # Prints List

friends.extend(numbers)         # extend function appends another list to the end
friends.append("Creed")         # Appends another item to the end of a list
friends.insert(1, "Kelly")      # Inserts an item into a specific index & pushes the other elements up
friends.remove("Jim")           # Removes a specific item by name
friends.pop()                   # Removes the last element in a list
print(friends.index("Kevin"))   # Checks if a certain item is in the list
print(friends.count("Jim"))     # Prints out the amount of times a certain item appears in the list
friends.sort()                  # Sorts the list in alphabetical (or for ints, ascending) order
numbers.reverse()               # reverses a list

friends2 = friends.copy()       # Copies a list into a variable

friends.clear()                 # Clears the entire list
