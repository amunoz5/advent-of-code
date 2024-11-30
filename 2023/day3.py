import re

with open("data/test.txt") as f:
    data = [line[:-1]+"." for line in f]

def is_symbol(data, i, j):
    return data[i][j] in "+$*#/%@-&=" if j>=0 and j<len(data[0]) and i>=0 and i<len(data) else False

def is_gear(data, i, j):
    if j<0 or j>=len(data[0]) and i>=0 and i<len(data):
        return False
    return data[i][j] == "*" and numbers_around(data, i, j) == 2
    
def numbers_around(data, i, j):
    has_right = j+1<len(data)
    has_left = j-1>=0
    has_top = i+1<len(data)
    has_bottom = i-1>=0
    
    # right and left
    numbers_around = 1 if has_right and data[i][j+1] in "0123456789" else 0
    numbers_around += 1 if has_left and data[i][j-1] in "0123456789" else 0
    
    # top
    if has_top and data[i+1][j] in ".+$*#/%@-&=":
        numbers_around += 1 if has_right and data[i+1][j+1] in "0123456789" else 0
        numbers_around += 1 if has_left and data[i+1][j-1] in "0123456789" else 0
    elif has_top:
        if (has_left and data[i+1][j-1] in "0123456789") or data[i+1][j] in "0123456789" or (has_right and data[i+1][j+1] in "0123456789"):
            numbers_around += 1
    # bottom 
    if has_bottom and data[i-1][j] in ".+$*#/%@-&=":
        numbers_around += 1 if has_right and data[i-1][j+1] in "0123456789" else 0
        numbers_around += 1 if has_left and data[i-1][j-1] in "0123456789" else 0
    elif has_bottom:
        if (has_left and data[i-1][j-1] in "0123456789") or data[i-1][j] in "0123456789" or (has_right and data[i-1][j+1] in "0123456789"):
            numbers_around += 1
    return numbers_around

number = ""
symbol_adjacent = False
suma = 0
gear_suma = 0

for i in range(len(data)):
    print()
    print(data[i-1] if i-1>=0 else ".")
    print(data[i])
    print(data[i+1] if i+1 < len(data) else ".")
    for j in range(len(data[i])):
        # if still reading number
        if data[i][j] in "0123456789":
            number += data[i][j]
            
            # look for symbols around
            symbols_sides = is_symbol(data, i, j-1) or is_symbol(data, i, j+1)
            symbols_up_down = is_symbol(data, i+1, j) or is_symbol(data, i-1, j)
            symbols_corners = is_symbol(data, i+1, j-1) or is_symbol(data, i-1, j-1) or is_symbol(data, i+1, j+1) or is_symbol(data, i-1, j+1) 
            char_symbol_adjacent = symbols_sides or symbols_up_down or symbols_corners
            symbol_adjacent = symbol_adjacent or char_symbol_adjacent
            
        # if reading . or symbol
        else:
            # process last number
            if number !="" and symbol_adjacent:
                print("n:", number)
                suma += int(number)
            number = ""
            symbol_adjacent = False
            
            if is_gear(data, i, j):
                print("is gear", data[i][j])
            
print("first star:", suma)
print("second star:", gear_suma)

# A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.
# you need to find the gear ratio of every gear and add them all up


