import sys
with open("input5.txt") as inp:
    data = inp.read()
    lines = data.split('\n')
    seeds = [int(x) for x in lines[0].split(" ")[1:]]
    curr_q = []
    for i in range(0,len(seeds)-1,2):
        curr_q.append((seeds[i], seeds[i+1]))
    index = 1
    transition = []
    while index < len(lines):
        if lines[index] == "":
            index += 1
        elif lines[index].find("map") != -1:
            if transition != []:
                next_q = []
                while len(curr_q) > 0:
                    start, count = curr_q.pop()
                    found = False
                    for tran in transition:
                        if tran[1] <= start <tran[1]+tran[2]:
                            found = True
                            if tran[1]+tran[2] < start + count:
                                next_q.append((tran[0]+start-tran[1], tran[1]+tran[2]-start))
                                curr_q.append((tran[1]+tran[2], count-(tran[1]+tran[2]-start)))
                            else:
                                next_q.append((tran[0]+start-tran[1], count))
                    if not found:
                        next_q.append((start, count))
                curr_q = next_q.copy()
                print(curr_q)
                transition = []
            index += 1
        else:
            transition.append([int(x) for x in lines[index].split(" ")])
            index += 1
    min = sys.maxsize
    for (start,_)in curr_q:
        if start< min:
            min = start
    print(min)