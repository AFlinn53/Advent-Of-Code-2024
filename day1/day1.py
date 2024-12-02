

with open('i1.txt') as f:
    text = f.read()



left_list = []
right_list = []

lines = text.splitlines()

for line in lines:
    left,right = line.split()
    
    left_list.append(int(left))
    right_list.append(int(right))

left_list.sort()
right_list.sort()

value = 0
for i in range(len(lines)):
    
    value += abs(left_list[i] - right_list[i])

print(value)