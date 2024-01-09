import re

with open("data/input1.txt") as f:
    data = [line[:-1] + "a" for line in f]

star1, star2 = 0, 0

number_dict = { 'one': '1', 'two': '2', 'three': '3', 'four': '4',
    'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9' }

def func(x): return x[0] + number_dict[x] + x[-1]

pattern = re.compile('|'.join(number_dict.keys())) #one|two|three ...       

for line in data:
    line1 = re.sub("[a-z]", "", line) + ""
    star1 += int(line1[0])*10 + int(line1[-1])
    
    line = pattern.sub(lambda x: func(x.group()), line)
    line = pattern.sub(lambda x: func(x.group()), line)
    line = re.sub("[a-z]", "", line) + ""
    star2 += int(line[0])*10 + int(line[-1])
    
print("first star:", star1, "\nsecond star:", star2)
