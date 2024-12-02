import collections


with open('i1.txt') as f:
    text = f.read()


map = collections.defaultdict(int)

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
freq = 0

for i in range(len(lines)):

    value += abs(left_list[i] - right_list[i])


for i in left_list:
    map[i] = 0

for i in right_list:
    map[i] += 1

for i in left_list:
    freq += (i*map[i])
    

print(value)
print(freq)