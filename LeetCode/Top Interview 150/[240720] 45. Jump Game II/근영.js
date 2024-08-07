var jump = function(nums) {
    let maxCoverage = 0;
    let lastIdx = 0;
    let target = nums.length - 1;
    let jump = 0;

    if(nums.length === 1) return 0;

    for(let i = 0; i < nums.length; i++){
        maxCoverage = Math.max(maxCoverage, i + nums[i]);
        
        if(i === lastIdx){
            lastIdx = maxCoverage;
            jump++;

            if(maxCoverage >= target){
                return jump;
            }
        }
    }

    return jump
};

// 어렵다,,,
