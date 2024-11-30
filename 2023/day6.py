with open("data/input6.txt") as f:
    data = [line[:-1].split()[1:] for line in f]

data_1 = [0, 0]
data_1[0] = [int(x) for x in data[0]] # time
data_1[1] = [int(x) for x in data[1]] # max distance so far

star1 = 1
i = 0
for max_time in data_1[0]:
    n_wins = 0
    max_distance = data_1[1][i]
    for time_holding in range(1, max_time):
        
        speed = time_holding # mm/ms
        travel_time = max_time - time_holding
        distance = travel_time * speed
        
        if distance > max_distance:
            n_wins += 1
        
    i += 1
    #print(max_time, time_holding, n_wins)
    star1 = star1 * n_wins 

print(star1)

star2 = 0
max_time = int("".join(data[0])) # time
max_distance = int("".join(data[1])) # max distance so far

for time_holding in range(1, max_time):
    star2 += 1 if (max_time - time_holding) * time_holding > max_distance else 0
print(star2)
