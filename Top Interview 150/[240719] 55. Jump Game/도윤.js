var canJump = function(nums) {
    
    let result = false;
    let jumpIdx = 0;

    for(let i = 0; i < nums.length; i++) {

        if( i > jumpIdx ) {
            return false;
        }

        jumpIdx = Math.max(jumpIdx, i + nums[i]);

        if (jumpIdx >= nums.length - 1) { 
            result = true;
        }

       
    }

    return result    
};

canJump([3,2,1,0,4]);
 