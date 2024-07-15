// 2024.07.15.
// https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150

// 근영
var removeElement = function(nums, val) {
    let idx = 0;

    for(let i = 0; i < nums.length; i++){
        if(nums[i] !== val){
            nums[idx] = nums[i];
            idx++
        } 
    }
    return idx
  
};