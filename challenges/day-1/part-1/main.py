nums = []

f = open("input.txt", "r")
nums = f.readlines()
f.close

for x in nums:
    for n in nums:
        if (int(x) + int(n) == 2020):
            print(int(x) * int(n))