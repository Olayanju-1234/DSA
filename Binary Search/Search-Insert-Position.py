

# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not,
# return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

def searchInsert(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return lo


print(searchInsert([5, 6, 7, 2, 8, 9], 10))
