import re

with open('i3.txt') as f:
    text = f.read()


#text = "mul(1,2)do()mul(3,4)do()"

pattern = "mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)"

groups = re.findall(pattern,text)

total = 0
compute = True

for seg in groups:
    if(seg == "do()"):
        compute = True
    if(seg == "don't()"):
        compute = False

    if(compute == True and seg != 'do()'):
        digit1,digit2 = re.findall("[0-9]+",seg)
        total += int(digit1) * int(digit2)


print(total)

