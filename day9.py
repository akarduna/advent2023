with open("input9.txt") as inp:
    data = inp.read()
    lines = data.split("\n")
    sum = 0
    for line in lines:
        vals = [[int(x) for x in line.split(" ")]]
        done = False
        while not done:
            nextVals = []
            done = True
            for i in range(len(vals[-1])-1):
                val = vals[-1][i+1]-vals[-1][i]
                if val != 0:
                    done = False
                nextVals.append(val)
            vals.append(nextVals)
        for i in range(len(vals)-2, -1, -1):
            vals[i].insert(0,vals[i][0]-vals[i+1][0])
        sum += vals[0][0]
        print(vals)
    print(sum)