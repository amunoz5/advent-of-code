with open("data/input6.txt") as f:
    data = [line[:-1].split()[1:] for line in f]

times = [int(x) for x in data[0]]
distances = [int(x) for x in data[1]]

star1, star2 = 1, 0
i = 0
for max_time in times:
    n_wins = 0
    n_wins += sum([
            1 if (max_time - time_holding) * time_holding > distances[i] else 0
            for time_holding in range(1, max_time)
            ])
    i += 1
    star1 = star1 * n_wins 

max_time = int("".join(data[0]))
max_distance = int("".join(data[1]))

for time_holding in range(1, max_time):
    star2 += 1 if (max_time - time_holding) * time_holding > max_distance else 0

print("first star:", star1, "\nsecond star:", star2)
