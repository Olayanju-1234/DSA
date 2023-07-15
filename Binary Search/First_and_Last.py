# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given
# target value.
#
# If target is not found in the array, return [-1, -1].
#
# You must write an algorithm with O(log n) runtime complexity.


def searchRange(nums: [int], target: int):
    result = [-1, -1]

    # Binary search for the leftmost occurrence of the target
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            result[0] = mid
            right = mid - 1  # Search left side for any earlier occurrences
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # If the target is not found, return [-1, -1]
    if result[0] == -1:
        return result

    # Binary search for the rightmost occurrence of the target
    left = result[0]
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            result[1] = mid
            left = mid + 1
        else:
            right = mid - 1

    return result


print(searchRange([5, 7, 7, 8, 8, 10], 8))
print(searchRange([5, 7, 7, 8, 8, 10], 6))
print(searchRange([], 0))
print(searchRange([1], 1))