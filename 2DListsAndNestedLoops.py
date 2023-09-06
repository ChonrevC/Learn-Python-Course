
# A 2D List is a list of lists
# Allows for a grid-like structure
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[0][0])            # 1
print(number_grid[2][1])            # 8

#######################################################
# Nested For-Loops

# This for loop should print out every number in the grid
for row in number_grid:
    for col in row:
        print(col)
