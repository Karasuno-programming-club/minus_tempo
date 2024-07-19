// 2024.07.16.
// https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150

var removeDuplicates = function (nums) {
  let k = 0;
  for (let i = 0; i < nums.length; i++) {
    // 정상적인 상황일 때
    if (nums[i] !== nums[i + 2]) {
      nums[k] = nums[i];
      k++;
    }
  }
  return k;
};

// time : O(N)
// space : O(1)

// index 2가 큰 값과 현재 값이 다르면 -> k를 이동시키며 값을 넣어준다
