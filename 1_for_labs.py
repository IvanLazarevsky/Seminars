def convert(array: list):
    return {value: [k for k in range(i, len(array)) if (value == array[k])] for i, value in enumerate(array) if
            (array.index(value)) >= i}


print(convert(['a', 'b', 'c', 'd', 'e', 'a', 'a', 'b', 'c']))
