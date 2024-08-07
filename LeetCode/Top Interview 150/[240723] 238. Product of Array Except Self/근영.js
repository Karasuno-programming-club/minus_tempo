var productExceptSelf = function (nums) {
  const length = nums.length;
  const left = new Array(length).fill(1);
  const right = new Array(length).fill(1);

  for (let i = 1; i < length; i++) {
    left[i] = left[i - 1] * nums[i - 1];
  }

  for (let i = length - 2; i >= 0; i--) {
    right[i] = right[i + 1] * nums[i + 1];
  }

  for (let i = 0; i < length; i++) {
    nums[i] = left[i] * right[i];
  }

  return nums;
};

// 나눗셈 쓰고 풀었다가 아차함
// 곱셈 DP는 처음인데 이걸 어떻게 처음에 생각할 수 있는건지 모르겠음 ㅠㅠ
