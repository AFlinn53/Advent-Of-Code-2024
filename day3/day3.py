import re

with open('i3.txt') as f:
    text = f.read()


#text = "mul(1,2)mul(3,4)"

pattern = "mul\([0-9]+,[0-9]+\)"

groups = re.findall(pattern,text)

total = 0;

for seg in groups:
    digit1,digit2 = re.findall("[0-9]+",seg)
    total += int(digit1) * int(digit2)


print(total)

