class hand():
    def __init__(self, inp) -> None:
        self.order = 'J23456789TQKA'
        self.h = inp.split(" ")[0]
        self.h_copy = self.h
        self.b = int(inp.split(" ")[1])
        self.rank = -1
        jocker = self.h.count('J')
        self.h = self.h.replace("J", "")
        if jocker == 5:
            self.h = self.h_copy
        elif jocker != 0:
            l = "1"
            m = 0
            for c in self.h:
                if self.h.count(c) > m:
                    l = c
                    m = self.h.count(c)
            self.h += l*jocker
        if len(set(self.h)) == 1:
            self.rank = 7
        elif self.h.count(self.h[0]) == 4 or self.h.count(self.h[1]) == 4:
            self.rank = 6
        elif len([x for x in self.h if self.h.count(x) ==3 or self.h.count(x) == 2]) == 5:
            self.rank = 5
        elif len([x for x in self.h if self.h.count(x) ==3]) == 3:
            self.rank = 4
        elif len([x for x in self.h if self.h.count(x) ==2]) == 4:
            self.rank = 3
        elif len([x for x in self.h if self.h.count(x) ==2]) == 2:
            self.rank = 2
        elif len(set(self.h)) == len(self.h):
            self.rank = 1
        self.h = self.h_copy
    def __lt__(self, other):
        if self.rank == other.rank:
            for i in range(len(self.h)):
                if self.order.find(self.h[i]) != self.order.find(other.h[i]):
                    return self.order.find(self.h[i]) < self.order.find(other.h[i])
        return self.rank < other.rank

with open("input7.txt") as inp:
    data = inp.read()
    lines = data.split("\n")
    hands = []
    for line in lines:
        h = hand(line)
        hands.append(h)
    hands.sort()
    sum = 0
    for i in range(len(hands)):
        sum += (i+1)*hands[i].b
    print(sum)