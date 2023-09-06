
# Try-Except is underutilized in my current programs. Use them more
# Try-Except makes it so it's easier to tell where a program goes wrong & plays except when it does

try:
    value = 10/0                                        # 10/0 is a ZeroDivisionError
    number = int(input("Enter a number: "))             # Putting in a string here would cause a ValueError
    print(number)

# as err lets us print out the except in error format
# just "except" by itself is bad practice
except ZeroDivisionError as err:                        # Python lets us do excepts based on the type of error
    print("Can't divide by 0!")

except ValueError as err:
    print("You put in the wrong letter!")
