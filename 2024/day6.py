with open("data/day6.txt") as file:
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

#3rd try 2nd star
star_2 = 0
MAX_STEPS = len(mapa)*len(mapa[0])

def in_loop(mapa, pos_guard, dir_guard):
    # in a loop if my position already has the expected symbol
    current_symbol = mapa[pos_guard[0]][pos_guard[1]]
    new_symbol = dir_mark[(dir_guard[0],dir_guard[1])]
    return current_symbol == '+' or current_symbol == new_symbol

def update_symbol(mapa, pos_guard, dir_guard):
    #print("[update_symbol]", pos_guard, dir_guard)
    current_symbol = mapa[pos_guard[0]][pos_guard[1]]
    new_symbol = dir_mark[(dir_guard[0],dir_guard[1])]
    if current_symbol == '#':
        print("[update_symbol] ERROR: trying to step on #. Pos:",pos_guard)
        return
    if current_symbol != '.' and current_symbol != new_symbol:
        new_symbol = '+'
    if (pos_guard[0]+dir_guard[0] in range(len(mapa)) and #in mapa
        pos_guard[1]+dir_guard[1] in range(len(mapa[0])) and
        mapa[pos_guard[0]+dir_guard[0]][pos_guard[1]+dir_guard[1]] == '#'):
        new_symbol = '+'
        
    mapa[pos_guard[0]][pos_guard[1]] = new_symbol
    return mapa

def walk(mapa, start_pos, start_dir):
    pos_guard = start_pos
    dir_guard = start_dir
    steps = 0
    visited = set()
    
    while (steps < MAX_STEPS and # just in case
           pos_guard[0]+dir_guard[0] in range(len(mapa)) and #in mapa
           pos_guard[1]+dir_guard[1] in range(len(mapa[0]))):
    
        next_pos = [pos_guard[0]+dir_guard[0],pos_guard[1]+dir_guard[1]]
        # If there is something directly in front of you, turn right 90 degrees.
        if mapa[next_pos[0]][next_pos[1]] == '#':
            dir_guard = rotate[str(dir_guard[0])+str(dir_guard[1])]
        # Otherwise, check loop and take a step forward.
        else:
            if (tuple(next_pos), tuple(dir_guard)) in visited:#start_pos == next_pos and dir_guard == start_dir: #in_loop(mapa, next_pos, dir_guard)
                return pos_guard, dir_guard, 1
            visited.add((tuple(next_pos), tuple(dir_guard)))
            pos_guard = next_pos
            mapa = update_symbol(mapa, pos_guard, dir_guard)
            steps += 1
        
    # state is 0 if out of mapa
    #          1 if found loop
    return pos_guard, dir_guard, 0

import time
from copy import deepcopy

steps = 0
#take a step. put an obstacle in front. walk. if loop, count loop. remove obstacle and continue.
while (steps < MAX_STEPS and # just in case
       pos_guard[0]+dir_guard[0] in range(len(mapa)) and #in mapa
       pos_guard[1]+dir_guard[1] in range(len(mapa[0]))):
    
    # take a step
    #print_map(mapa)
    #print("- step",steps)
    #print("Walking")
    next_pos = [pos_guard[0]+dir_guard[0],pos_guard[1]+dir_guard[1]]
    # If there is something directly in front of you, turn right 90 degrees.
    if mapa[next_pos[0]][next_pos[1]] == '#':
        dir_guard = rotate[str(dir_guard[0])+str(dir_guard[1])]
    # Otherwise, check loop and take a step forward.
    else:
   
        # put an obstacle in front
        mapa_copy = deepcopy(mapa)
        new_obs_pos = [pos_guard[0]+dir_guard[0],pos_guard[1]+dir_guard[1]]
        if new_obs_pos[0] not in range(len(mapa)) or new_obs_pos[1] not in range(len(mapa[0])):
            break
        mapa_copy[new_obs_pos[0]][new_obs_pos[1]] = '#'
        #print("obstacle in",new_obs_pos)
    
        #walk
        _,_,state = walk(mapa_copy, pos_guard, dir_guard)
        #print("obstacle state", state)
    
        # if loop, count loop.
        if state>0:
            star_2 += 1 if new_obs_pos != start_pos else 0
            #mapa_copy[new_obs_pos[0]][new_obs_pos[1]] = 'O'
            #print_map(mapa_copy)
            #print("LOOP!", new_obs_pos)
        # remove obstacle and continue
        pos_guard = next_pos
        mapa = update_symbol(mapa, pos_guard, dir_guard)
        steps += 1
        #time.sleep(1)

#1st star
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
# time for star 2 -> 52 min so far (result 656 too low, 1885 is too high) NOT: 1616
# time for day 5 ->   min
