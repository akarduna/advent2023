import numpy as np
with open("input13.txt") as inp:
    data = inp.read()
    lines = data.split("\n")
    patterns = []
    curr_pattern = []
    for line in lines:
        if len(line) == 0:
            patterns.append(np.array(curr_pattern))
            curr_pattern = []
        else:
            curr_pattern.append(list(line))
    patterns.append(np.array(curr_pattern))
    sum = 0
    for p,pattern in enumerate(patterns):
        vert = 0
        vert_p = 0 
        horiz = 0
        horiz_p = 0
        valid = [i for i in range(1,len(pattern[0]))]
        loc = (-1,-1)
        for i in valid:
            dist = min(len(pattern[0])-i, i)
            if np.array_equal(pattern[: ,i-dist:i], pattern[: ,i+dist-1:i-1:-1]):
                    vert = i
        valid = [i for i in range(1,len(pattern))]
        for i in valid:
            dist = min(len(pattern)-i, i)
            if np.array_equal(pattern[i-dist:i,:], pattern[i+dist-1:i-1:-1,:]):
                    horiz = i    
        for j in range(len(pattern)):
            for k in range(len(pattern[0])):
                new_pattern = pattern.copy()
                new_pattern[j][k] = "#" if pattern[j][k] == "." else "."
                valid = [i for i in range(1,len(new_pattern))]
                for i in valid:
                    dist = min(len(new_pattern)-i, i)
                    if i!= horiz and  np.array_equal(new_pattern[i-dist:i,:], new_pattern[i+dist-1:i-1:-1,:]):
                        horiz_p = i
                        loc = (j,k)
        for k in range(len(pattern[0])):
            for j in range(len(pattern)):
                new_pattern = pattern.copy()
                new_pattern[j][k] = "#" if pattern[j][k] == "." else "."
                valid = [i for i in range(1,len(new_pattern[0]))]
                for i in valid:
                    dist = min(len(new_pattern[0])-i, i)
                    if i!= vert and  np.array_equal(new_pattern[: ,i-dist:i], new_pattern[: ,i+dist-1:i-1:-1]):
                        vert_p = i
        sum += (horiz_p*100 + vert_p)
    print(sum)
                
        