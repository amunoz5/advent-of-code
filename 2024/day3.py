import re

with open("data/day3.txt") as file:
    line= file.read().strip()
#    lines = [l.strip() for l in file]

star_1 = 0
for (a,b) in re.findall(r"mul\(([0-9]*),([0-9]*)\)",line):
    star_1+=int(a)*int(b)

next_do = True
star_2=0
for instr in re.split(r"(don't\(\)|do\(\))", line):
    if instr == "do()":
        next_do=True
        continue
    
    if instr=="don't()":
        next_do=False
        continue
    
    if next_do:
        matches = re.findall(r"mul\(([0-9]*),([0-9]*)\)",instr)
        for (a,b) in matches:
            star_2+=int(a)*int(b)

print("star 1:",star_1)
print("star 2:",star_2)

# time for star 1 -> 10:18 min
# time for star 2 -> 16:47 min
# time for day 3 -> 27:05 min
