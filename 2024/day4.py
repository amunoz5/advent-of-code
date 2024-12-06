
with open("data/day4.txt") as file:
#    line= file.read().strip()
    grid = [l.strip() for l in file]


def around(grid, i, j, letter, star):
    lista = []
    directions = directions_1 if star==1 else directions_2
    for [x, y] in directions:
        if (i+x in range(len(grid)) and j+y in range(len(grid[0])) and
              grid[i+x][j+y] == letter):
            lista += [[x,y]]
    return lista

def find(grid, i0, j0, direction, word):
    x,y = direction
    i,j = i0,j0
    #if in range and match, look for next letter
    if (len(word)>0 and
          i+x in range(len(grid)) and j+y in range (len(grid[0])) and
          grid[i+x][j+y] == word[0]):
        return find (grid, i+x, j+y, direction, word[1:] )
    #if word is done, found!
    return len(word)==0        


directions_1 = [[-1,-1],[-1,0],[-1,1],
                [0,-1],        [0,1],
                [1,-1], [1,0], [1,1]]

directions_2 = [[-1,-1],[-1,1],
                [1,-1], [1,1]]

def star_1():
    word ="XMAS"
    num_found = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # get first letter & direction
            if grid[i][j] == word[0]:
                match_directions = around(grid, i, j, word[1], 1)
                for direction in match_directions:
                    # if you find the rest of the word
                    if find(grid, i, j, direction, word[1:]):
                        num_found += 1
    return num_found

def star_2():
    word="MAS"
    num_found = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # get second letter & direction
            if grid[i][j] == word[1]:
                match_directions = around(grid, i, j, word[2], 2)
                if len(match_directions)<=1:
                    continue
                all_good = True
                for direction in match_directions:
                    all_good =( all_good and
                            i-direction[0] in range(len(grid)) and
                            j-direction[1] in range(len(grid[0])) and
                                # 1st letter opposite to direction
                            grid[i-direction[0]][j-direction[1]]==word[0] and
                                # and full word from 2nd letter on
                            find(grid, i-direction[0], j-direction[1], direction, word[1:])
                               )
                num_found += 1 if all_good else 0
    return num_found

print("star 1:", star_1())
print("star 2:", star_2())

# time for star 1 -> >40 min
# time for star 2 -> >30 min
# time for day 4 -> :( min
