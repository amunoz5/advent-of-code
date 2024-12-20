with open("data/test.txt") as file:
    mapa = [list(l.strip()) for l in file]

# position of the guard and direction of movement
pos_dir = {"^": [-1, 0],
           "v": [1, 0],
           ">": [0, 1],
           "<": [0, -1]}

#get starting position & direction
pos_guard =[-1, -1]
for x in range(len(mapa)):
    for y in range(len(mapa[x])):
        if mapa[x][y] in pos_dir.keys():
            pos_guard = [x,y]
start_pos = pos_guard
            
dir_guard = pos_dir[mapa[pos_guard[0]][pos_guard[1]]]
rotate = {"-10": [0, 1], # [-1, 0]:[0, 1]
           "01": [1, 0],
           "10": [0, -1],
          "0-1": [-1, 0]}

# while moving, if colliding with line perpendicular to direction and
# continuing that path does not step on start pos, it's a loop!
dir_mark = {(-1, 0): "|",
            (1, 0):"|",
            (0, 1):"-",
            (0, -1):"-"}

def print_map(mapa):
    for row in mapa:
        print(''.join([x for x in row]))


def collision_origin(mapa, pos, direction, rot):
    '''
    Checks if this trajectory collides with the origin point
    '''
    #print("[collision origin]-->", pos, direction, rot)
    #print_map(mapa)
    #if rotation, rotate
    if rot:
        direction = rotate[str(direction[0])+str(direction[1])]
    found=False
    #while in mapa and left  
    while ("".join([x for row in mapa for x in row]).count(".")>0 and
           pos[0]+direction[0] in range(len(mapa)) and
           pos[1]+direction[1] in range(len(mapa[0])) and
           mapa[pos[0]][pos[1]] != '#'):
        found = found or mapa[pos[0]][pos[1]] not in pos_dir.keys()
        pos = [pos[0]+direction[0],pos[1]+direction[1]]
    return found and mapa[pos[0]][pos[1]] != '#'
#1st try 2nd star
"""
star_2 = 0
# move while in map and map has .s
while ("".join([x for row in mapa for x in row]).count(".")>0 and
       pos_guard[0]+dir_guard[0] in range(len(mapa)) and
       pos_guard[1]+dir_guard[1] in range(len(mapa[0]))):

    next_pos = [pos_guard[0]+dir_guard[0],pos_guard[1]+dir_guard[1]]
    
    # If there is something directly in front of you, turn right 90 degrees.
    if mapa[next_pos[0]][next_pos[1]] == '#':
        dir_guard = rotate[str(dir_guard[0])+str(dir_guard[1])]
        mapa[pos_guard[0]][pos_guard[1]] = '+'
        
    # Otherwise, take a step forward.
    else:
        # if colliding with line perpendicular to yours and not starting pos, possible loop
        if (mapa[next_pos[0]][next_pos[1]] not in pos_dir.keys() and
            mapa[next_pos[0]][next_pos[1]] in dir_mark.values() and
            mapa[next_pos[0]][next_pos[1]] != mapa[pos_guard[0]][pos_guard[1]]):
            #if following direction does not make me collide with starting pos before obstacle, loop
            if not collision_origin(mapa.copy(), next_pos, dir_guard,True):
                                  #  mapa[next_pos[0]][next_pos[1]] == '#'):
                star_2 +=1
                print_map(mapa)
                print()
            #if I collided with starting pos, obstacle could be placed on its side
            
        
        #mark current position as stepped on (except starting pos)
        if mapa[next_pos[0]][next_pos[1]] not in pos_dir.keys():
            pos_guard = next_pos
            mapa[pos_guard[0]][pos_guard[1]] = dir_mark[(dir_guard[0],dir_guard[1])]
        else:
            pos_guard = next_pos
        
"""
#2nd try 2nd star
#for each position while walking, what if we put an obstacle in front?
#rotate to the right, and if you find your own path before finding an obstacle => loop
star_2 = 0
MAX_STEPS = len(mapa)*len(mapa[0])

def collision_origin_v2(mapa, pos, direction):
    '''
    Checks if this trajectory finds a . before a +
    '''
    aux = rotate[str(direction[0])+str(direction[1])]
    other_line = dir_mark[(aux[0],aux[1])]
    found = False
    steps = 0
    #while in mapa and not found obstacle  
    while (steps < MAX_STEPS and
           #"".join([x for row in mapa for x in row]).count(".")>0 and
           pos[0]+direction[0] in range(len(mapa)) and
           pos[1]+direction[1] in range(len(mapa[0])) and
           not found):
        # |-+ followed by . is not ok
        found = (mapa[pos[0]][pos[1]] in list(dir_mark.values())+['+'] and
                mapa[pos[0]+direction[0]][pos[1]+direction[1]] == '.')
        pos = [pos[0]+direction[0],pos[1]+direction[1]]
        steps +=1
    print("[check collision origin 2] position found:", pos,start_pos)
    return found #and pos[0] != start_pos[0] and pos[1] != start_pos[1]

def collision_my_path(mapa, pos, direction):
    '''
    Checks if this trajectory collides with a previously walked path (same orientation)
    '''
    #print("[collision path]-->", pos, direction)
    #print_map(mapa)

    #Always rotate
    direction = rotate[str(direction[0])+str(direction[1])]
        
    found = False
    steps = 0
    #while in mapa and not found obstacle  
    while (steps < MAX_STEPS and
           #"".join([x for row in mapa for x in row]).count(".")>0 and
           pos[0]+direction[0] in range(len(mapa)) and
           pos[1]+direction[1] in range(len(mapa[0])) and
           mapa[pos[0]][pos[1]] != '#' and not found):
        found = (mapa[pos[0]][pos[1]] == dir_mark[(direction[0], direction[1])]
                 or mapa[pos[0]][pos[1]] == '+')
        pos = [pos[0]+direction[0],pos[1]+direction[1]]
        steps +=1
        
    return found and not collision_origin_v2(mapa, pos, direction)

#
steps = 0
while (steps < MAX_STEPS and
       #"".join([x for row in mapa for x in row]).count(".")>0 and
       pos_guard[0]+dir_guard[0] in range(len(mapa)) and
       pos_guard[1]+dir_guard[1] in range(len(mapa[0]))):
    
    next_pos = [pos_guard[0]+dir_guard[0],pos_guard[1]+dir_guard[1]]
    # If there is something directly in front of you, turn right 90 degrees and take a step.
    if mapa[next_pos[0]][next_pos[1]] == '#':
        mapa[pos_guard[0]][pos_guard[1]] = '+'
        dir_guard = rotate[str(dir_guard[0])+str(dir_guard[1])]
        pos_guard = [pos_guard[0]+dir_guard[0],pos_guard[1]+dir_guard[1]]
    # Otherwise, check possible obstable in front. Also, take a step forward.
    else:
        if collision_my_path(mapa, pos_guard, dir_guard):
            print_map(mapa)
            print("loop!")
            star_2 += 1
        if  mapa[pos_guard[0]][pos_guard[1]] in ['|','-']:
            mapa[pos_guard[0]][pos_guard[1]] = '+'
        else:
            mapa[pos_guard[0]][pos_guard[1]] = dir_mark[(dir_guard[0],dir_guard[1])]
        pos_guard = next_pos
        steps += 1


"""
# move while in map and map has .s
while ("".join([x for row in mapa for x in row]).count(".")>0 and
       pos_guard[0]+dir_guard[0] in range(len(mapa)) and
       pos_guard[1]+dir_guard[1] in range(len(mapa[0]))):

    next_pos = [pos_guard[0]+dir_guard[0],pos_guard[1]+dir_guard[1]]
    # If there is something directly in front of you, turn right 90 degrees.
    if mapa[next_pos[0]][next_pos[1]] == '#':
        dir_guard = rotate[str(dir_guard[0])+str(dir_guard[1])]
    # Otherwise, take a step forward.
    else:
        mapa[pos_guard[0]][pos_guard[1]] = 'X'
        pos_guard = next_pos
        
#print(pos_guard, dir_guard)

#How many distinct positions will the guard visit before leaving the mapped area?

print("star 1:", "".join([x for row in mapa for x in row]).count("X")+1)
"""
print("star 2:", star_2)

# time for star 1 -> 21.59 min
# time for star 2 -> 52 min so far (result 656 too low)
# time for day 5 ->   min
