# One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.

def oneAway(str1, str2):
    if len(str1) == len(str2):
        return oneEditReplace(str1, str2)
    elif len(str1) + 1 == len(str2):
        return oneEditInsert(str1, str2)
    elif len(str1) - 1 == len(str2):
        return oneEditInsert(str2, str1)
    return False


def oneEditReplace(str1, str2):
    foundDifference = False
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            if foundDifference:
                return False
            foundDifference = True
    return True


def oneEditInsert(str1, str2):
    index1 = 0
    index2 = 0
    while index2 < len(str2) and index1 < len(str1):
        if str1[index1] != str2[index2]:
            if index1 != index2:
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1
    return True


print(oneAway("pale", "ple"))
print(oneAway("pales", "pale"))
print(oneAway("pale", "bale"))
print(oneAway("pale", "bake"))
