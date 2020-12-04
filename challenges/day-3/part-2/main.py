input = []

f = open("input.txt", "r")
input = f.read().splitlines()
f.close

slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
treeCounts = []

for s in slopes:
    treeCount = 0
    i = 0
    xPos = 0
    while i < len(input):
        base = input[i]

        while (xPos + 3) >= (len(input[i])):
            input[i] += base

        if input[i][xPos] == '#':
            treeCount += 1

        xPos += s[0]
        i += s[1]

    treeCounts.append(treeCount)

multiply = 1

for m in treeCounts:
    multiply = multiply * m
    
print(multiply)