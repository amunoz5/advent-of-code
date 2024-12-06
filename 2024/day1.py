
with open("data/day1.txt") as file:
    lines = [l.strip().split("   ") for l in file]


col1 = [int(i[0]) for i in lines]
col2 = [int(i[1]) for i in lines]

star2 = 0
for elem in col1: 
    star2 += col2.count(elem) * elem

col1.sort()
col2.sort()

dist = [abs(col1[i]-col2[i]) for i in range(len(col1))]

print("star 1:", sum(dist))
print("star 2:", star2)

# time for star 1 -> 11:27 min
# time for star 2 -> 05:59 min
# time for day 1 -> 17:28 min
