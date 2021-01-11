l = ['hcl:#623a2f', 'ecl:hzl', 'hgt:168cm', 'pid:795434985', 'eyr:2020', 'iyr:2020', 'cid:209', 'byr:1970'], ['cid:325', 'byr:2007', 'eyr:1933', 'hgt:188in', 'pid:713080083', 'ecl:#d624ca', 'iyr:2030', 'hcl:z'], ['hcl:#7d3b0c', 'pid:431742871', 'ecl:hzl', 'hgt:169cm', 'cid:340', 'eyr:2023', 'iyr:2017', 'byr:1994']

d =[]
for num in range(len(l)):

    d.append([num.split(":") for num in l[num]])
    
    
#for num in range(len(d))
print(len(d))
print(d[0][0][0])
odd = []
even = []
for num in range(len(d)):
    for x in range(len(d[num])):
        for s in range(len(d[num][x])):
            #print(d[num][x][s])
            if s % 2 == 0:
                odd.append(d[num][x][s])
            elif s % 2 == 1:
                even.append(d[num][x][s])

print("Odd is", odd)
print("even is", even)

zipped = zip(odd, even)

diczip = dict(zipped)
print(diczip)