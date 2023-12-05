with open("input1.txt") as inp:
    data = inp.read()
    sum = 0
    for line in data.split('\n'):
        nums = []
        for i in range(len(line)):
            c = line[i]
            if c.isnumeric():
                nums.append(int(c))
            if line[i:].find("one") == 0:
                nums.append(1)
            if line[i:].find("two") == 0:
                nums.append(2)
            if line[i:].find("three") == 0:
                nums.append(3)
            if line[i:].find("four") == 0:
                nums.append(4)
            if line[i:].find("five") == 0:
                nums.append(5)
            if line[i:].find("six") == 0:
                nums.append(6)
            if line[i:].find("seven") == 0:
                nums.append(7)
            if line[i:].find("eight") == 0:
                nums.append(8)
            if line[i:].find("nine") == 0:
                nums.append(9)
        if len(nums) < 1:
            print(line)
        elif len(nums) == 1:
            sum += nums[0]*10 + nums[0]
        else:
            sum += nums[0]*10 + nums[-1]
    print(sum)