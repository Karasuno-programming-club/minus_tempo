/**
 * @param {number[]} nums
 * @return {number}
 */
var jump = function(nums) { 
    let cnt = 0;
    let jumpIdx = 0;
    let farthest = 0;

    if(nums.length === 1) return cnt;

    for(let i = 0; i < nums.length; i++) {
        
        farthest = Math.max(farthest, i + nums[i]);
        
        // 매번 최대 거리에 도달할 때 마다 cnt 증가
        if(i == jumpIdx) {
            cnt++;
            jumpIdx = farthest;
        }
        
        if (jumpIdx >= nums.length - 1) { 
            return cnt
        }
    }

    return cnt;
};  

console.log(jump([7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]))