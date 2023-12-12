with open("input10.txt") as inp:
    data = inp.read()
    lines = data.split("\n")
    graph = []
    start = (-1,-1)
    distances = []
    for i,line in enumerate(lines):
        row = []
        for j,char in enumerate(line):
            if char == 'S':
                start = (i,j)
                row.append(((1,0), (-1,0), (0,1), (0,-1)))
            elif char == "|":
                row.append(((1,0), (-1,0)))
            elif char == "-":
                row.append(((0,1), (0,-1)))
            elif char == "L":
                row.append(((-1,0), (0,1)))
            elif char == "J":
                row.append(((-1,0), (0,-1)))
            elif char == "7":
                row.append(((1,0), (0,-1)))
            elif char == "F":
                row.append(((1,0), (0,1)))
            else:
                row.append(())
        graph.append(row)
        distances.append([-1]*len(row))
    distances[start[0]][start[1]] = 0
    nodes = []
    for (i,j) in graph[start[0]][start[1]]:
        for (x,y) in graph[start[0]+i][start[1]+j]:
            if x == -i and y == -j:
                nodes.append(((start[0]+i, start[1]+j),1))
    m = -1
    while len(nodes)>0:
        node, dist = nodes[0]
        nodes = nodes[1:]
        if distances[node[0]][node[1]]!= -1:
            m = max(m, distances[node[0]][node[1]])
        else:
            distances[node[0]][node[1]] = dist
            for (i,j) in graph[node[0]][node[1]]:
                if 0<= node[0] + i <len(graph) and 0 <= node[1] +j < len(graph[0]):
                    if distances[node[0]+i][node[1]+j] == -1:
                        nodes.append(((node[0]+i, node[1]+j),dist+1))
    curr_node = start
    direction = (-1,-1)
    for (i,j) in graph[start[0]][start[1]]:
        if 0<= start[0] + i < len(graph) and 0 <= start[1] +j < len(graph[-1]):
            for (x,y) in graph[start[0]+i][start[1]+j]:
                if x == -i and y == -j:
                    direction = (i,j)
                    break
        if direction != (-1,-1):
            break
    #print(curr_node,direction)
    init_direction = direction
    curr_node = (start[0] + direction[0], start[1] + direction[1])
    total_rotations = [0,0]
    included = []
    for row in distances:
        r =  [False]*len(distances[-1])
        included.append(r)
    while curr_node != start:
        d_save = direction
        for (x,y) in graph[curr_node[0]][curr_node[1]]:
            if -d_save[0] != x or -d_save[1] != y:
                if -d_save[1] == x and d_save[0] == y:
                    total_rotations[0] += 1
                    direction = (x,y)
                    break
                elif d_save[1] == x  and -d_save[0] == y:
                    total_rotations[1] += 1
                    direction =(x,y)
                    break
        d_new = (d_save[1], -d_save[0])
        temp_node = (curr_node[0] + d_new[0], curr_node[1] + d_new[1])
        while distances[temp_node[0]][temp_node[1]] == -1:
            included[temp_node[0]][temp_node[1]] = True
            temp_node = (temp_node[0]+d_new[0], temp_node[1]+d_new[1])
        d_new = (direction[1], -direction[0])
        temp_node = (curr_node[0] + d_new[0], curr_node[1] + d_new[1])
        while distances[temp_node[0]][temp_node[1]] == -1:
            included[temp_node[0]][temp_node[1]] = True
            temp_node = (temp_node[0]+d_new[0], temp_node[1]+d_new[1])
        curr_node = (curr_node[0] +direction[0], curr_node[1] +direction[1])
        #print(curr_node, direction)
    count = 0
    for i in range(len(included)):
        for j in range(len(included[-1])):
            if included[i][j]:
                count +=1
    print(count)