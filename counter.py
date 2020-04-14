

# @deprecated
def countChars(string):
    # Create empty container for chars
    chars = {}
    for char in string:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    return chars


def findPairs(findChars, string):
    counter = 0

    for char in string:
        if char in findChars:
            counter += 1

    return counter


def percent(first, second):
    return round(first / (first + second) * 100)
