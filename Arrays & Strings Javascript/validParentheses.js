/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let newNums = []
    for (let i=0; i < nums.length; i++) {
        newNums.push(nums[i])
        if (newNums.includes(nums[i+1])) {
            return true
        }
    }
    return false
};

console.log(containsDuplicate([1,5,5,2,3,1]))

