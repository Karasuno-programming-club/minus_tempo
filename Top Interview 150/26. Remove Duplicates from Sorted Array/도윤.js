/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
  
    let p = 0;

    for (let i = 1; i < nums.length; i++) {
        if (nums[i] !== nums[p]) {
            p++;
            nums[p] = nums[i];
        }
    }

    return i + 1;
}; 

removeDuplicates([0,0,1,1,1,2,2,3,3,4]); // 5