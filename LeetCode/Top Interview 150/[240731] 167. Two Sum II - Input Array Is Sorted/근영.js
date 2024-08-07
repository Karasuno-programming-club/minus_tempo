var twoSum = function (numbers, target) {
  let first = 0;
  let second = numbers.length - 1;

  while (numbers[first] + numbers[second] !== target) {
    if (numbers[first] + numbers[second] > target) {
      second--;
    } else {
      first++;
    }
  }

  return [first + 1, second + 1];
};

// 난 왜 이렇게 바보인걸까..
