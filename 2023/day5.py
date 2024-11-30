with open("data/input5.txt") as f:
    data = [line[:-1] for line in f] + [""]

# seed -> soil -> fertilizer -> water -> light -> temperature -> humidity -> location

def next_section(line_start):
    line = line_start
    while data[line] != "":
        line += 1
    return line + 1

seeds = [int(x) for x in data[0].split()[1:]]

steps = [[s]+[0]*7 for s in seeds] 
line = 0
step_i = -1

for seed in seeds:
    line = next_section(line) + 1
    step_i += 1 # seed
    step_j = 1  # section (soil, fertilizer, water, ...

    for k in range(8):
        in_range = False
        look_for = steps[step_i][k]
        
        # look for mapping
        while not in_range and data[line] != "":
            dest_start, source_start, len_range = [int(x) for x in data[line].split()]
            if look_for >= source_start and look_for <= source_start + len_range:
                in_range = True
                steps[step_i][step_j] = dest_start - source_start + look_for
                step_j += 1
            line += 1
            
        # unmapped => destination = source
        if not in_range:
            steps[step_i][step_j] = look_for
            step_j += 1
            
        if step_j >= 8:
            line = 0
            break
        line = next_section(line) + 1
    #print(seed,":",steps[step_i])

print("first star:", min([steps[i][-1]for i in range(len(steps))]))

# I'm running out of memory :(
import gc
del steps
gc.collect()

def run2(seeds_2):
    # only save prev step
    steps = [s for s in seeds_2]
    line = 0
    step_i = -1
    
    for seed in seeds_2:
        line = next_section(line) + 1
        step_i += 1 # seed
        step_j = 1  # section (soil, fertilizer, water, ...
    
        for _ in range(8):
        
            in_range = False
            look_for = steps[step_i]
        
            # look for mapping
            while not in_range and data[line] != "":
                dest_start, source_start, len_range = [int(x) for x in data[line].split()]
                if look_for >= source_start and look_for <= source_start + len_range:
                    in_range = True
                    steps[step_i] = dest_start - source_start + look_for
                    step_j += 1
                line += 1
            
            # unmapped => destination = source
            if not in_range:
                steps[step_i] = look_for
                step_j += 1
            
            if step_j >= 8:
                line = 0
                break
            line = next_section(line) + 1
        #print(seed,":",steps[step_i])
    return min([last for last in steps])

seeds_intervals = [[seeds[x], seeds[x] + seeds[x+1]] for x in range(0, len(seeds), 2) ]

# I'll iterate in 1000 numbers chunks to avoid memory errors
num_seeds = 0 #2 549 759 327
for [init, end] in seeds_intervals:
    num_seeds += end-init

global_min = 999999999999
iterations = 0
MAX_SEEDS = 100000
next_seed = [0, 0] #[idx of interval in seeds_intervals, idx of elem in interval]
while iterations < num_seeds:
    
    seeds_2 = []
    for _ in range(MAX_SEEDS):
        next_interval = seeds_intervals[next_seed[0]]
        next_elem = next_interval[0] + next_seed[1]
        if next_elem in range(next_interval[0], next_interval[1]):
            seeds_2 += [next_elem]
            next_seed[1] += 1
        else:
            seeds_2 += seeds_intervals[next_seed[0] + 1]
            next_seed[0] += 1
            next_seed[1] = 1

    new_min = run2(seeds_2)
    global_min = min(global_min, new_min)
    #print("global min:", global_min, "new min:", new_min)
    iterations += MAX_SEEDS


print("second star:",global_min )

