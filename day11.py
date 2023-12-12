import numpy as np
def get_val(i,j, arr):
    if i > j:
        return get_val(j,i, arr)
    if arr[i][j] == -1:
        arr[i][j] = get_val(i, i,arr) + get_val(i+1, j,arr)
        return arr[i][j]
    else:
        return arr[i][j]
with open("input11.txt") as inp:
    data = inp.read()
    lines = data.split("\n")
    galaxies = []
    num_blank_rows = np.zeros((len(lines),len(lines)), dtype=int)-1
    num_blank_cols = np.zeros((len(lines),len(lines)), dtype=int)-1
    row_blank = [True]*len(lines)
    col_blank = [True]*len(lines[-1])
    for row,line in enumerate(lines):
        for col,val in enumerate(line):
            if val == "#":
                blank = False
                galaxies.append((row,col))
                row_blank[row] = False
                col_blank[col] = False
    for i,row in enumerate(row_blank):
        if row:
            num_blank_rows[i][i] = (1000000-1)
        else:
            num_blank_rows[i][i] = 0
    for i, col in enumerate(col_blank):
        if col:
            num_blank_cols[i][i] = (1000000-1)
        else:
            num_blank_cols[i][i] = 0
    sum = 0
    for i in range(len(galaxies)):
        for j in range(i+1,len(galaxies)):
            row_diff = galaxies[j][0]-galaxies[i][0] +get_val(galaxies[j][0], galaxies[i][0], num_blank_rows)
            ma = max(galaxies[j][1],galaxies[i][1])
            mi = min(galaxies[j][1],galaxies[i][1])
            col_diff = ma - mi + get_val(ma,mi, num_blank_cols)
            sum += row_diff + col_diff
    print(sum)