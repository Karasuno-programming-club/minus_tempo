var maxArea = function (height) {
  let left = 0;
  let right = height.length - 1;
  let answer = 0;

  while (left < right) {
    let w = right - left;
    let h = Math.min(height[left], height[right]);

    if (answer < w * h) {
      answer = w * h;
    }

    if (height[left] > height[right]) right--;
    else left++;
  }

  return answer;
};

// 이런게 greedy 군..
