def NFA_Checker(inp, state_list, counts):
    new_states = []
    new_counts = []
    if len(inp) == 0 or len(state_list) == 0:
        return state_list,counts
    for i,state in enumerate(state_list):
        s = []
        if len(state) >= 1:
            s = [int(e) for e in state.split(" ")]
        if inp[0] == "#" or inp[0]=="?":
            if len(s) >= 1:
                s[0] -= 1
                if s[0] >= 0:
                    s[-1] = 1
                    st = " ".join(str(e) for e in s)
                    found = False
                    for j,new_st  in enumerate(new_states):
                        if st == new_st:
                            found = True
                            new_counts[j] += counts[i]
                    if not found:
                        new_states.append(st)
                        new_counts.append(counts[i])
        s = []
        if len(state) >= 1:
            s = [int(e) for e in state.split(" ")]
        if inp[0] == "." or inp[0] == "?":
            st = "NULL"
            if len(s) > 1 and s[0] == 0:
                s[-1] = 0
                st = " ".join(str(e) for e in s[1:])
            elif len(s) > 1 and s[-1] == 0:
                st = " ".join(str(e) for e in s)
            elif len(s) == 1 and s[-1] == 0:
                st = " ".join(str(e) for e in s)
            if st != "NULL":
                found = False
                for j,new_st  in enumerate(new_states):
                    if st == new_st:
                        found = True
                        new_counts[j] += counts[i]
                if not found:
                    new_states.append(st)
                    new_counts.append(counts[i])
    return NFA_Checker(inp[1:], new_states, new_counts)
with open("input12.txt") as inp:
    data = inp.read()
    lines = data.split("\n")
    dic = {}
    s = 0
    for line in lines:
        tot = 0
        springs, spec = line.split(" ")
        spec = [int(s) for s in spec.split(",")]*5
        springs = (springs + "?")*4 + springs
        states, counts = NFA_Checker(springs, [" ".join(str(e) for e in spec) + " 0"], [1])
        for i in range(len(states)):
            if len(states[i]) == 0:
                tot += counts[i]
            elif len(states[i]) == 1 and states[i] == "0":
                tot += counts[i]
            elif len(states[i]) == 3 and states[i] == '0 1':
                tot += counts[i]
        s += tot
    print(s)