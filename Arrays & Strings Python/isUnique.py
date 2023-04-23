# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?

def isUnique(str):
    str = str.lower()
    sortedString = sorted(str)
    for i in range(len(sortedString) - 1):
        if sortedString[i] == sortedString[i+1]:
            return False
    return True


# print(isUnique("world"))
