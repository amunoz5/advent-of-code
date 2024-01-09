import re

with open("data/input2.txt") as f:
    data = [line[:-1] for line in f]

bag = {"red": 12, "green": 13, "blue": 14}
star1, star2 = 0, 0

for line in data:
    games = [re.split(", ", game) for game in re.split(": |; ", line)[1:]]
    possible = True
    min_bag =  {"red": 0, "green": 0, "blue": 0}
    
    for game in games:
        for pick in game:
            num = re.search("\d+", pick).group()
            colour = re.search("green|red|blue", pick).group()
            possible = possible and bag[colour] >= int(num)
            min_bag[colour] = max(int(num), min_bag[colour])
    
    star1 += int(re.search("Game (\d+): ", line).group(1)) if possible else 0
    star2 += min_bag["red"] * min_bag["green"] * min_bag["blue"]

print("first star:", star1, "\nsecond star:", star2)
