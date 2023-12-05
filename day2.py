with open("input2.txt") as inp:
    data = inp.read()
    sum = 0
    ammount = [14, 12, 13]
    for line in data.split('\n'):
        game_num = int("".join([c for c in line.split(": ")[0] if c.isnumeric()]))
        bags = line.split(": ")[1].split(";")
        nums = [0]*3
        for bag in bags:
            num = ""
            for i in range(len(bag)):
                if (bag[i].isnumeric()):
                    num = num + bag[i]
                elif bag[i:].find("blue") == 1:
                    nums[0] = max(nums[0], int(num))
                    num = ""
                elif bag[i:].find("red") == 1:
                    nums[1] = max(nums[1], int(num))
                    num = ""
                elif bag[i:].find("green") == 1:
                    nums[2] = max(nums[2], int(num))
                    num = ""
        sum += nums[0]*nums[1]*nums[2]
    print(sum)