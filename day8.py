import math
with open("input8.txt") as inp:
    graph = {}
    data = inp.read()
    lines = data.split("\n")
    directions = lines[0]
    lines = lines[1:]
    curr_node = []
    for line in lines:
        if line != "":
            if line.find("="):
                key = line.split(" ")[0]
                if key[-1] == "A":
                    curr_node.append(key)
                left = line.split(" ")[2][1:-1]
                right = line.split(" ")[3][:-1]
                graph[key] = (left, right)
    curr_node_copy = curr_node[:]
    lengths = []
    for c in curr_node_copy:
        curr_node = [c]
        prev = 0
        steps = 0
        index = 0
        done = False
        while not done and steps <9999999:
            done = True
            if directions[index] == "L":
                for i in range(len(curr_node)):
                    curr_node[i] = graph[curr_node[i]][0]
                    if curr_node[i][-1] != "Z":
                        done = False
            else:
                for i in range(len(curr_node)):
                    curr_node[i] = graph[curr_node[i]][1]
                    if curr_node[i][-1] != "Z":
                        done = False
            index += 1
            index = index % len(directions)
            steps +=1
            if done:
                done = False
                if prev != 0:
                    lengths.append(steps-prev)
                    done = True
                prev = steps

    print(math.lcm(*lengths))
