def check(inp):
    return not( inp.isnumeric() or inp == '.')
with open("input3.txt") as inp:
    data = inp.read()
    sum = 0
    scheme = []
    nums = []
    gears = []
    for row,line in enumerate(data.split('\n')):
        l = []
        curnum = ""
        curn = [0,row,0,0, False]
        for col,c in enumerate(line):
            if c == "*":
                gears.append([row,col])
            if c.isnumeric():
                if curnum == "":
                    curn[2] = col
                curnum += c
            elif curnum != "":
                curn[0] = int(curnum)
                curn[3] = col
                nums.append(curn.copy())
                curn = [0,row,0,0, False]
                curnum = ""
            l.append(c)
        if curnum != "":
            curn[0] = int(curnum)
            curn[3] = col
            nums.append(curn.copy())
        scheme.append(l)
    for num in nums:
        valid = False
        for i in range(num[2]-1, num[3]+1):
            valid += check(scheme[max(0,num[1]-1)][min(max(0,i), len(scheme[i])-1)])
            valid += check(scheme[num[1]][min(max(0,i), len(scheme[i])-1)])
            valid += check(scheme[min(len(scheme)-1,num[1]+1)][min(max(0,i), len(scheme[i])-1)])
        if valid:
            num[-1] = True
    for gear in gears:
        count = 0
        val = 1
        for num in nums:
            if abs(num[1]-gear[0]) <= 1 and gear[1]>= num[2]-1 and gear[1] <= num[3] and nums[-1]:
                val*= num[0]
                count += 1
                print(num)
        if count == 2:
            sum += val
    print(sum)