# You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There
# are at least two different characters in letters.
#
# Return the smallest character in letters that is lexicographically greater than target. If such a character does
# not exist, return the first character in letters.

def nextGreatestLetter(letters: [str], target: str) :
    left = 0
    right = len(letters) - 1

    if target >= letters[right]:
        return letters[0]

    while left <= right:
        mid = (left + right) // 2

        if letters[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1

    return letters[left]


print(nextGreatestLetter(["c", "f", "j"], "a"))
print(nextGreatestLetter(["c", "f", "j"], "c"))




