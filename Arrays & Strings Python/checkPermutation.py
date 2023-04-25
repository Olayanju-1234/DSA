# 2 Check Permutation: Given two strings, write a method to decide if one is a permutation of the
# other

#def checkPermutation(str1, str2):
#     str1 = sorted(str1)
#     str2 = sorted(str2)
#     print(str1, str2)
#     if str1 == str2:
#         return True
#     return False
#
#
# print(checkPermutation("madam est", "madam est"))

def checkPermutation(str1, str2):
    if len(str1) != len(str2):
        return False

    str_dict = {}

    for string in str1:
        if string in str_dict:
            str_dict[string] += 1
        else:
            str_dict[string] = 1

    for k in str2:
        if k in str_dict:
            str_dict[k] -= 1
            if str_dict[k] < 0:
                return False
        else:
            return False

    for count in str_dict.values():
        if count != 0:
            return False

    return True


print(checkPermutation("tac", "cat"))
