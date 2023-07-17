# We are playing the Guess Game. The game is as follows:
#
# I pick a number from 1 to n. You have to guess which number I picked.
#
# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
#
# You call a pre-defined API int guess(int num), which returns three possible results:
# -1: Your guess is higher than the number I picked (i.e. num > pick).
# 1: Your guess is lower than the number I picked (i.e. num < pick).
# 0: your guess is equal to the number I picked (i.e. num == pick).
# Return the number that I picked


def guess():
    pass


def guessNumber(n: int) -> int:
    left = 1
    right = n
    while left <= right:
        mid = (left + right) // 2
        if guess() == 0:
            return mid
        elif guess() == 1:
            left = mid + 1
        else:
            right = mid - 1
    return left


print(guessNumber(10))
print(guessNumber(1))
print(guessNumber(2))
