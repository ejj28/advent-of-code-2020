input = []

f = open("input.txt", "r")
input = f.read().splitlines()
f.close

requiredTags = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

entries = []

tags = []
for i in input:
    
    if not i.strip():
        entries.append(tags)
        tags = []
    else:
        for x in range(len(i)):
            if i[x] == ':':
                tags.append(i[x-3:x])

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