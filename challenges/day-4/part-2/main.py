input = []

f = open("input.txt", "r")
input = f.read().splitlines()
f.close

requiredTags = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

entries = []

tags = {}
for i in range(len(input)):
    
    if input[i] == "":
        entries.append(tags)
        tags = {}
    else:
        for x in range(len(input[i])):
            if input[i][x] == ':':
                s = x
                while input[i][s] != " ":
                    s += 1
                    if s == len(input[i]):
                        break
                tags[input[i][x-3:x]] = input[i][x+1:s]
    if i == len(input) - 1:
        entries.append(tags)
        tags = {}

entriesWithRequiredTags = []

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
        entriesWithRequiredTags.append(e)

zcount = 0
for z in entriesWithRequiredTags:
    compliance = False
    if len(z["byr"]) == 4 and int(z["byr"]) >= 1920 and int(z["byr"]) <= 2002:
        if len(z["iyr"]) == 4 and int(z["iyr"]) >= 2010 and int(z["iyr"]) <= 2020:
            if len(z["eyr"]) == 4 and int(z["eyr"]) >= 2020 and int(z["eyr"]) <= 2030:
                if (z["hgt"][-2:] == "in" and int(z["hgt"][:-2]) >= 59 and int(z["hgt"][:-2]) <= 76) or (z["hgt"][-2:] == "cm" and int(z["hgt"][:-2]) >= 150 and int(z["hgt"][:-2]) <= 193):
                    if (len(z["hcl"]) == 7 and z["hcl"][0] == "#" and z["hcl"][1:].isalnum()):
                        eyeC = z["ecl"]
                        validColours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                        cValid = False
                        for c in validColours:
                            if eyeC == c:
                                cValid = True
                                break
                        if cValid == True:
                            if len(z["pid"]) == 9:
                                zcount += 1
print(zcount)