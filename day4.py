with open("input4.txt") as inp:
    data = inp.read()
    sum = 0
    counts = [1]*len(data.split("\n"))
    for row,line in enumerate(data.split('\n')):
        winning, have = line.split(": ")[1].split(" | ")
        winning = [int(w) for w in winning.split(" ") if w != ""]
        have = [int(h) for h in have.split(" ") if h != ""]
        count = 0
        for h in have:
            if h in winning:
                count += 1
        for i in range(1,count+1):
            if (i +row < len(counts)):
                counts[i+row] += counts[row]
        sum += counts[row]
    print(sum)