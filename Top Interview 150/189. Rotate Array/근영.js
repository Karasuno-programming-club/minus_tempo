// 2024.07.17.
// https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150

var rotate = function (nums, k) {
  let length = nums.length;
  let rotateNum = nums.length - (k % nums.length);

  for (let i = 0; i < rotateNum; i++) {
    nums[i + length] = nums[i];
  }

  for (let i = 0; i < rotateNum; i++) {
    nums.shift();
  }
};
