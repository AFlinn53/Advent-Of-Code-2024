with open('i2.txt') as f:
    text = f.read()


lines = text.splitlines()


data = [[int(x) for x in i.split(" ")] for i in lines]


# data = [
#     [7, 6, 4, 2, 1],
#     [1, 2, 7, 8, 9],
#     [9, 7, 6, 2, 1],
#     [1, 3, 2, 4, 5],
#     [8, 6, 4, 4, 1],
#     [1, 3, 6, 7, 9]
# ]

count = 0;

for row in data:

    increasing = all(1 <= (j - i) <= 3 for i, j in zip(row, row[1:]))
    decreasing = all(1 <= (i - j) <= 3 for i, j in zip(row, row[1:]))

    if (increasing == True or decreasing == True):
        count += 1


print(count)



# test = [1,2,3,6]
# test2 = [7,6,5,2]

# increasing = all(i - j < 0 and i-j > -4 for i, j in zip(test, test[1:]))
# print(increasing)

# descreasing = all(i - j < 4 and i - j > 0 for i, j in zip(test2, test2[1:]))
# print(descreasing)

#     if(increasing)
    
    # for i, sublist in zip(row, [row[i + 1:] for i in range(len(row))]):
    #     for j in sublist: 
    #         diff = abs(i - j)
    #         if diff > 3 or diff == 0:
    #             count += 1
    #             break

# print(count)




