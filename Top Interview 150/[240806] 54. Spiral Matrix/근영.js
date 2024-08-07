var spiralOrder = function (matrix) {
  let n = matrix.length;
  let m = matrix[0].length;
  let answer = [];

  let curX = 0; // position of x
  let curY = 0; // position of y

  while (answer.length < matrix.length * matrix[0].length) { //m n 값을 사용하면안됨

    console
    // 정방향
    if (curX !== m) {

      for (let i = 0; i < m; i++) {
        answer.push(matrix[curY][i]);
        curX = i;
      }
      curY++;

      for (let i = curY; i < n; i++) {
        answer.push(matrix[i][curX]);
        curY = i;
      }
    } else { //역방향
      console.log('역방향');
      console.log(answer);
      for (let i = curX; i >= curX - m; i--) {
        answer.push(matrix[curY][i]);
        curX = i;
      }
      curY--;

      for (let i = curY; i >= curY - n; i--) {
        answer.push(matrix[i][curX]);
        curY = i;
      }
    }

    m--;
    n--;
  }

  return answer;
};

spiralOrder([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
]);
