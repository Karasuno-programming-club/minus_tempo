// 2024.07.15.
// https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/1321844823/?envType=study-plan-v2&envId=top-interview-150

// 근영
var removeDuplicates = function(nums) {
    let k = 0;
    for(let i = 1; i < nums.length; i++){
        if(nums[k] < nums[i]){
            nums[k+1] = nums[i];
            k++;
        }
    }
    return k+1;
};