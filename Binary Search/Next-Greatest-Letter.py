def nextGreatestLetter(letters, target):
    firstLetter, lastLetter = 0, len(letters) - 1

    while firstLetter <= lastLetter:
        mid = (firstLetter + lastLetter) // 2

        middleLetter = letters[mid]

        # print(mid, middleLetter)

        if middleLetter == target:
            print(middleLetter, target)
            return middleLetter

        elif middleLetter < target:
            firstLetter = mid + 1

        elif middleLetter > target:
            lastLetter = mid - 1

    return firstLetter


print(nextGreatestLetter(["k", "l", "m", "n", "o"], "m"))