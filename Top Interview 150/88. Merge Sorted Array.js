// 2024.07.15.
// https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

// 근영
var merge = function(nums1, m, nums2, n) {    
    let curIdx = m + n - 1;
    m--;
    n--;

    while(n >= 0){
        if(nums1[m] > nums2[n]){
            nums1[curIdx] = nums1[m];
            m--;
        } else {
            nums1[curIdx] = nums2[n];
            n--;
        }
        curIdx--;
    }
};