var minSubArrayLen = function (target, nums) {
  let left = 0;
  let sum = 0;
  let distance = Infinity;

  for (let right = 0; right < nums.length; right++) {
    sum += nums[right];

    while (sum >= target) {
      distance = Math.min(distance, right - left + 1);
      sum -= nums[left];
      left++;
    }
  }
  return distance === Infinity ? 0 : distance;
};
