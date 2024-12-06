
with open("data/day2.txt") as file:
    lines = [list(map(int, l.strip().split(" "))) for l in file]

# BOTH:
#    The levels are either all increasing or all decreasing.
#    Any two adjacent levels differ by at least one and at most three.

def check_safety(report):
    # order dictated by first non equal pair
    found = False
    i = 0
    while not found and i<len(report)-1:
        i+=1
        found = not report[i-1]==report[i]
    increasing = report[i-1]<report[i]
    
    all_good = True
    for i in range(1,len(report)):
        if not all_good:
            break
        
        num = abs(report[i-1]-report[i])
        if increasing:
            all_good = report[i-1]<report[i] and num>0 and num<4
        else:
            all_good = report[i-1]>report[i] and num>0 and num<4
             
    return all_good

star_1 = [1 if check_safety(x) else 0 for x in lines]
star_1 = sum(star_1)

star_2 = 0
for report in lines:
    #safe if it finished
    if check_safety(report):
        star_2 +=1
    # if it didnt, remove one by one and check safety
    else:
        small_good = False
        i=0
        while not small_good and i<len(report):
            small_report = report.copy()
            del small_report[i]
            small_good = check_safety(small_report)
            i+=1
        star_2 +=1 if small_good else 0

print("star 1:",star_1)
print("star 2:",star_2)

# time for star 1 -> 28:40 min
# time for star 2 -> 10:24 min
# time for day 2 -> 39:04 min
