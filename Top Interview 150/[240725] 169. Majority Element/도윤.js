/**
 * @param {number[]} nums
 * @return {number}
 */

var majorityElement = function(nums) {
    let majorityNum = nums.length/2;
    nums.sort();

    for (let i = 0; i < nums.length; i++) {
        
        if(nums[i] != nums[i-1]) {
            majorityNum = nums.length/2;  
        }

        majorityNum--;

        if(majorityNum <= 0) return nums[i]
    }
};

majorityElement([3,2,3]);