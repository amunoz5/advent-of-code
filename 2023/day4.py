import re

with open("data/input4.txt") as f:
    data = [[1] + re.sub('Card \d: ', '', line[:-1]).split('|') for line in f]
    
star1 = 0
for i in range(len(data)):
    
    match = 0
    winner = data[i][1].strip().split()
    for num in data[i][2].strip().split():
        match += 1 if num in winner else 0
    star1 += 2**(match-1) if match > 0 else 0

    for _ in range(data[i][0]):
        for j in [x+1 for x in range(match)]:
            data[i+j][0] += 1
    
    #print(match, data[i][0],'\t',winner,'\t',data[i][2])
    
print("first star:", star1)
print("second star:", sum([data[i][0] for i in range(len(data))]))
