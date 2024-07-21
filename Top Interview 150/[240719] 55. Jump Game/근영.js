var canJump = function(nums) {
    let idx = 0;
    let max = 0;
    let target = nums.length - 1;

    // greedy
    // 점프할 수 있는 최대로 갔을 때 도달해야 함
    for(let i = 0; i < nums.length; i++){
        max = Math.max(max, idx + nums[i]);

        if(max >= target){
            return true;
        }

        if(max <= idx && nums[idx] === 0){
            return false;
        }
        idx++
    }

    return false
};