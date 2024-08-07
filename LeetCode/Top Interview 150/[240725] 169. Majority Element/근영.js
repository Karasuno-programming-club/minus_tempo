var majorityElement = function(nums) {
    const n = Math.ceil(nums.length / 2) - 1;
    nums.sort((a, b) => b - a);
    return nums[n]
};