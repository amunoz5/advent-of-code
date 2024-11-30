
with open("data/test.txt") as f:
    data = [line[:-1] for line in f]

#turning clockwise
pipes = {
    '|': { 'u': [[1, 0], [-1, 0]], # going up
           'd': [[-1, 0], [1, 0]], # going down
          },
    '-': {
          'r': [[0, -1], [0, 1]], # going right
          'l': [[0, 1], [0, -1]], # going left
          }
}
corners = { # 0: new_direction  1: prev_ij  2: next_ij
    'L': ["u", [0, 1], [-1, 0]],
    'J': ["l", [-1, 0], [0, -1]],
    '7': ["d", [0, -1], [1, 0]],
    'F': ["r", [1, 0], [0, 1]]
}

max_rows = len(data)
max_cols = len(data[0])
corners_list = "LJ7F"
pipes_list = "|-"

def find_s(data):
    for s_row in range(max_rows):
        for s_col in range(max_cols):
            if data[s_row][s_col] == 'S':
                return s_row, s_col

def find_next(i, j, dire, data, symbol=""):
    symbol = data[i][j] if symbol == "" else symbol
    if symbol in "|-":
        return pipes[symbol][dire][1] if dire in pipes[symbol].keys() else [99, 99]
    return corners[symbol][2] if symbol in "LJ7F" else [99, 99]

def find_prev(i, j, dire, data, symbol=""):
    symbol = data[i][j] if symbol == "" else symbol
    if symbol in "|-":
        return pipes[symbol][dire][0] if dire in pipes[symbol].keys() else [99, 99]
    return corners[symbol][1] if symbol in "LJ7F" else [99, 99]

def find_next_s(si, sj, data):
    for dire in "udrl":
        for s in "|-LJ7F":
            possible = False
            [next_di, next_dj] = find_next(si, sj, dire, data, symbol=s)
            [prev_di, prev_dj] = find_prev(si, sj, dire, data, symbol=s)
            
            if next_di < 99 and next_dj < 99 and prev_di < 99 and prev_dj < 99:
                prev_i = si + prev_di
                prev_j = si + prev_dj
                next_i = si + next_di
                next_j = sj + next_dj
                if data[prev_i][prev_j] in "|-LJ7F" and data[next_i][next_j] in "|-LJ7F":
                    
                    print(dire, s,":", [si+prev_di, sj+prev_dj], "->", [si+next_di, sj+next_dj])
                    print("      ", data[prev_i][prev_j], "->",data[next_i][next_j])
                    prev_next_ij = find_next(prev_i, prev_j, dire, data, symbol=s)
                    next_prev_ij = find_prev(next_i, next_j, dire, data, symbol=s)
                    print("     ", [prev_next_ij[0]+prev_i, prev_next_ij[1]+prev_j] , "->",[next_prev_ij[0]+next_i, next_prev_ij[1]+next_j] )
        """
        print("if s is", s,"move to", next_i, next_j)
        if next_i>=0 and next_j>=0 and next_i<max_rows and next_j<max_cols and prev_i>=0 and prev_j>=0 and prev_i<max_rows and prev_j<max_cols and data[next_i][next_j] in corners_list and data[prev_i][prev_j] in corners_list :
            print(actions[data[next_i][next_j]][0], [si, sj])
            print(actions[data[prev_i][prev_j]][1], [si, sj])"""
        print()
    return [999, 999]


#find s
s_row, s_col = find_s(data)
print("S:", s_row, s_col)

# loop
next_pos = find_next_s(s_row, s_col, data)
print("next_pos", next_pos)
"""
i = s_row
j = s_col
steps = 0
while i != s_row and j != s_col:
    print("in while")
    next_pos = find_next(i, j, data)
    i = next_pos[0]
    j = next_pos[1]
    steps += 1
    print(data[i][j])
"""

"""
steps_max = steps
steps = 0
while steps < steps_max//2 and i != s_row and j != s_col:
    next_pos = find_next(i, j, data)
    i = next_pos[0]
    j = next_pos[1]
    steps += 1
    """
