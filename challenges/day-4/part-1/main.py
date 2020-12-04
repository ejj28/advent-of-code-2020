input = []

f = open("input.txt", "r")
input = f.read().splitlines()
f.close

requiredTags = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

entries = []

tags = []
for i in range(len(input)):
    
    if input[i] == "":
        entries.append(tags)
        tags = []
    else:
        for x in range(len(input[i])):
            if input[i][x] == ':':
                tags.append(input[i][x-3:x])
    if i == len(input) - 1:
        entries.append(tags)
        tags = []

complianceCount = 0

for e in entries:
    compliance = True
    for t in requiredTags:
        match = False
        for tag in e:
            if tag == t:
                match = True
        if match == False:
            compliance = False
    if compliance == True:
        complianceCount += 1
print(complianceCount)