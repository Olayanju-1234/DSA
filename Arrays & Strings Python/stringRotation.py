# String Rotation:Assume you have a method isSubstring which checks if one word is a substring
# of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
# call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat")

def stringRotation(str1, str2):
    return len(str1) == len(str2) and str2 in str1 + str1


print(stringRotation("waterbottle", "erbottlewat"))
print(stringRotation("waterbottle", "erbottlewatt"))
