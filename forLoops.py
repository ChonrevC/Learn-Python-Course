# For-loops let us loop over different items

#For-loops don't support parantheses, unlike if-else statements and while loops
for letter in "Giraffe Acad":
    print(letter)

print()

friends = ["Jim", "Karen", "Kevin"]
for friend in friends:
    print(friend)

print()

# range gives us all numbers from 1st parameter to number before 10 (due to start form 0)
for number in range(3,10):
    print(number)

print()

for index in range(len(friends)):
    if(index == 0):
        print("First friend")
    else:
        print(friends[index])