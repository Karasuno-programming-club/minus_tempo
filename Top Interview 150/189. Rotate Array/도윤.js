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