/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {

    k = k % nums.length;

    // 마지막 K개를 저장한다
    const lastK = nums.slice(-k);

    // 남아있는 배열을 K만큼 밀어낸다 (순환)
    for(let i = (nums.length - 1); i > 0 ; i--) {
        nums[i] = nums[i-k];
    }

    // 마지막 K개를 앞에 넣는다
    for(let k = 0; k < lastK.length; k++) {
        nums[k] = lastK[k];
    }

};

rotate([1,2,3,4,5,6,7],3);

/**
 * 시간 복잡도 O(N)
 */

/**
 * reverse 방법
 */

var rotate2 = function(nums, k) {

    k = k % nums.length;

    const reverse = (nums, start, end) => {
        while(start < end) {
            let tmp = nums[start];
            nums[start] = nums[end];
            nums[end] = tmp;
            start++;
            end--;
        }  
    };

    reverse(nums, 0, nums.length - 1); // [7,6,5,4,3,2,1] 전체 reverse
    reverse(nums, 0, k - 1); // [5,6,7,4,3,2,1] 로테이션 숫자만 reverse
    reverse(nums, k, nums.length - 1); // [5,6,7,1,2,3,4] 나머지 숫자만 reverse  
};

rotate2([1,2,3,4,5,6,7],3);


/**
 * 시간 복잡도 O(n)
 */