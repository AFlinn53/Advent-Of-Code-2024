with open('i2.txt') as f:
    text = f.read()


lines = text.splitlines()


data = [[int(x) for x in i.split(" ")] for i in lines]

count = 0

for row in data:
    
    modified_rows = [row[:i] + row[i+1:] for i in range(len(row))]

    for modified_row in modified_rows:
        
        increasing = all(1 <= (j - i) <= 3 for i, j in zip(modified_row, modified_row[1:]))
        decreasing = all(1 <= (i - j) <= 3 for i, j in zip(modified_row, modified_row[1:]))
    
        if increasing or decreasing:
            count += 1
            break 

print(count)