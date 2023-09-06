# If statements are conditionals that check if certain values are true
#   if values are true, the code that is indented will run

# if statement with a boolean variable
is_male = True
is_tall = False


if is_male and is_tall:                             # and keyword lets us check if both values are true ("or" for if either one)
    print("You are male and tall")
elif is_male or not(is_tall):                            # "elif" stands for else if         # not() function negates value
    print("You are a male or not tall or both")
else:
    print("You are neither male nor tall")
