input = []

f = open("input.txt", "r")
input = f.read().splitlines()
f.close

xPos = 0

testarray = [4,2,3,4,5,6,7]
for t in range(len(testarray)):
    print(testarray[t])

treeCount = 0
linecount = 0
for i in range(len(input)):
    print(str(linecount) + " xpos:" + str(xPos))
    if xPos == 33:
        print(input[i])
    if input[i][xPos] == '#':
        treeCount += 1
    if i != len(input) - 1:
        length = len(input[i + 1])
        base = input[i]
        while (xPos + 3) >= (len(input[i + 1])):
            print("appending")
            input[i + 1] += base
            print(input[i + 1])
        xPos += 3
        linecount+=1

print("treecount:" + str(treeCount))
