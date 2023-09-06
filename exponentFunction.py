# the pow() function can also be used with ** (2**3 means 2^3)
# We can also do this by creating a function

def power(baseNum, powNum):
    
    result = 1
    for index in range(powNum):
        result *= baseNum

    return result

print(power(2, 3))