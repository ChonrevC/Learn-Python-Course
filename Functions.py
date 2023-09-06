# Functions are a collection of code that performs a specific task

# Create a function with def
def sayHi():                                        # The : means all code that comes indented after will be part of the function
    print("Hello user")

print("Top")
sayHi()                                             # Call the function
print("Bottom\n")

# Python also allows another function with the same name, but different parameters
def sayHi(name, age):
    print("Hello " + name + "! You are " + str(age) + " years old!")

sayHi("Mike", 47)
print()

# Sometimes when calling a function, we want info back from that function
def getCube(num):
    return pow(num, 3)

print(getCube(3))

