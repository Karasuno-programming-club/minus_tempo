/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    
    const left_arr = Array.from({ length: nums.length  }).fill(1);
    const right_arr = Array.from({ length: nums.length  }).fill(1);
    const result = Array.from({ length: nums.length  }).fill(1);
    const lastIdx = nums.length - 1;

    for (let i = 0; i < nums.length; i++) {

        // 첫번째의 경우 
        if (i === 0) {
            right_arr[lastIdx - 1] = right_arr[lastIdx] * nums[lastIdx];
            continue;
        }

        // 마지막케이스
        left_arr[i] = left_arr[i-1] * nums[i-1];
        right_arr[lastIdx - i] = right_arr[lastIdx -i +1] * nums[lastIdx -i +1];

    }


    for (let i = 0; i < nums.length; i++) {
        result[i] = left_arr[i] * right_arr[i];
    }

    return result;

};

productExceptSelf([1,2,3,4]);