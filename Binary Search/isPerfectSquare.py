# Given a positive integer num, return true if num is a perfect square or false otherwise.
#
# A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer
# with itself.
#
# You must not use any built-in library function, such as sqrt.

def isPerfectSquare(num):
    if num < 2:
        return True

    left, right = 2, num // 2

    while left <= right:
        mid = left + (right - left) // 2
        square = mid * mid

        if square == num:
            return True
        elif square < num:
            left = mid + 1
        else:
            right = mid - 1

    return False


print(isPerfectSquare(16))
print(isPerfectSquare(14))
print(isPerfectSquare(1))
