import re

with open("data/input1.txt") as f:
    data = [line[:-1]+"a" for line in f]

res = 0
for line in data:
    new_line = re.sub("[a-z]", "", line) + ""
    #print(line, new_line)
    line = new_line
    res += int(line[0])*10 + int(line[-1])
print("first star:",res)

number_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def func(x):
    return x[0] + number_dict[x] + x[-1]

res = 0

pattern = re.compile('|'.join(number_dict.keys())) #one|two|three ...
for line in data:
    new_line = pattern.sub(lambda x: func(x.group()), line)
    #print(line, " -> ", new_line)
    new_line = pattern.sub(lambda x: func(x.group()), new_line)
    #print(line, " -> ", new_line)
    new_new_line = re.sub("[a-z]", "", new_line) + ""
    #print(line, " -> ", new_line, new_new_line)
    line = new_new_line
    res += int(line[0])*10 + int(line[-1])

print("second star:",res)
