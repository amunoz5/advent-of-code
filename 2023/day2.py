import re

with open("data/input2.txt") as f:
    data = [line[:-1] for line in f]

def is_possible(games, bag):
    possible = True
    for game in games:
        for pick in game:
            num = re.search("\d+", pick).group()
            colour = re.search("green|red|blue", pick).group()
            possible = possible and bag[colour] >= int(num)
    return possible

def get_min_bag(games):
    min_bag =  {"red": 0, "green": 0, "blue": 0}
    for game in games:
        for pick in game:
            num = re.search("\d+", pick).group()
            colour = re.search("green|red|blue", pick).group()
            min_bag[colour] = max(int(num), min_bag[colour])
    return min_bag

bag = {"red": 12, "green": 13, "blue": 14}

res1 = 0
res2 = 0
for line in data:
    game_id = re.search("Game (\d+): ", line).group(1)
    games = [re.split(", ", game) for game in re.split(": |; ", line)[1:]]
    #print(game_id,":",games)
    if is_possible(games, bag):
        #print("possible\n")
        res1 += int(game_id)
    minimums = get_min_bag(games)
    #print("min config:", minimums)
    res2 += minimums["red"] * minimums["green"] * minimums["blue"]

print("first star:",res1)
print("second star:", res2)

