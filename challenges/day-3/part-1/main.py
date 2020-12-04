input = []

f = open("input.txt", "r")
input = f.read().splitlines()
f.close

xPos = 0

treeCount = 0

for i in range(len(input)):

    base = input[i]

    while (xPos + 3) >= (len(input[i])):
        input[i] += base

    if input[i][xPos] == '#':
        treeCount += 1

    xPos += 3

print(treeCount)
