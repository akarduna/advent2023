import math
with open("input6.txt") as inp:
    data = inp.read()
    lines = data.split("\n")
    #times = [int(x) for x in lines[0].split(": ")[1].split(" ") if x != ""]
    times = [int(lines[0].split(": ")[1].replace(" ", ""))]
    distances = [int((lines[1].split(": ")[1].replace(" ","")))]
    print(times)
    print(distances)
    #distances = [int(x) for x in lines[1].split(": ")[1].split(" ") if x != ""]
    product = 1
    for i in range(len(times)):
        mi = (((-times[i] + math.sqrt(times[i]**2-4*distances[i]))/-2))+0.001
        ma = (((-times[i] - math.sqrt(times[i]**2-4*distances[i]))/-2))-0.001
        mi = max(math.ceil(mi),0)
        ma = min(math.floor(ma), times[i])
        product *= (ma+1-mi)
    print(product)