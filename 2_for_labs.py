def jaccardSimiliarity(setA: set, setB: set):
    size = 0
    for item in setA:
        if item in setB:
            size += 1
    return size / (len(setA) + len(setB) - size)


print(jaccardSimiliarity({1, 2, 3, 5}, {1, 6, 2, 5}))
