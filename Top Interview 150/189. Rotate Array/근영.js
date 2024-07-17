// 2024.07.17.
// https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150

// 풀다보니 space complexity가 O(N)
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

// solutions
var rotate = function(nums, k) {
  k = k % nums.length; // k번만큼 로테이션 돌기 때문에 길이만큼 돌아도 결국 같음 -> 나머지만큼만 돌면됨

  const reverse = (i, j) => {
      while(i < j){
          let temp = nums[i];
          nums[i] = nums[j];
          nums[j] = temp;
          i++;
          j--;
      }
  }

  reverse(0, nums.length - 1);
  reverse(0, k-1);
  reverse(k, nums.length - 1);
};