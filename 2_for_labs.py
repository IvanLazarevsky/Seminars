def jaccardSimiliarity(setA: set, setB: set):
    size = 0
    for item in setA:
        if item in setB:
            size += 1
    return size / (len(setA) + len(setB) - size)
