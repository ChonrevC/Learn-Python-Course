# Instead of just booleans, we can compare strings and numbers in if statements using comparison operators

def maxNum(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    
    elif num2 >= num1 and num2 >= num3:
        return num2

    else:
        return num3

print(maxNum("dog", "doggo", "doggos"))
print(maxNum(3, 4, 5))


