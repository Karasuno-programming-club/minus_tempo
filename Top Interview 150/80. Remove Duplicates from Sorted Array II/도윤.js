/**
 * @param {number[]} nums
 * @return {number}
 */


var removeDuplicates = function (nums) {
  
    let k = 1;
    let cnt = 1;
    
    for(let i = 1; i < nums.length; i++ ) {
        if(nums[i] != nums[i-1]) {
            nums[k++] = nums[i];
            cnt = 1;
        } else {
            if(cnt < 2) {
                nums[k++] = nums[i];
                cnt ++
            }
        }
    }
    return k;
};


/**
 * 시간 복잡도 O(N)
 */
removeDuplicates([0,0,1,1,1,1,2,3,3]);


var removeDuplicates2 = function (nums) {
    let p = 0;

    for(let i = 0; i < nums.length; i++) {
        if(nums[i] != nums[i+2]) {
            nums[p] = nums[i];
            p++;
        } 
    }

    return p;
};

removeDuplicates2([0,0,1,1,1,1,2,3,3]);