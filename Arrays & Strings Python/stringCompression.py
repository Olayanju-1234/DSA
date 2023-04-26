# String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).

def stringCompression(string):
    # check if there are no digits in the string
    if any(char.isdigit() for char in string):
        return "no digits allowed in string"

    newString = ''
    count = 0

    for i in range(len(string)):
        count += 1

        if i + 1 >= len(string) or string[i] != string[i + 1]:
            newString += string[i] + str(count)
            count = 0

    return newString if len(newString) < len(string) else string


print(stringCompression("aaaabbbbccyyycc"))
