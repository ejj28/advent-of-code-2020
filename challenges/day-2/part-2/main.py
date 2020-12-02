input = []

f = open("input.txt", "r")
input = f.readlines()
f.close

complianceCount = 0

for i in input:
    dPos = 0
    sPos = 0
    lPos = 0
    loopCount = 0
    for x in i:
        if (x == '-'):
            dPos = loopCount
        elif (x == ' '):
            sPos = loopCount
        elif (x == ':'):
            lPos = loopCount - 1
            break
        loopCount += 1
    min = ""
    max = ""
    letter = ''
    password = ""

    letter = i[lPos]

    for y in range(0, dPos):
        min += i[y]
    for n in range(dPos + 1, sPos):
        max += i[n]
    for p in range(lPos + 3, len(i) - 1):
        password += i[p]

    if ((password[int(min) - 1] == letter) ^ (password[int(max) - 1] == letter)):
        complianceCount += 1

print(complianceCount)