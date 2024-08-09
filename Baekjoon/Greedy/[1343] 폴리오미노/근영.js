const INPUT = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

function solution() {
  const board = INPUT[0];
  let cnt = 0;
  let answer = "";

  for (let i = 0; i < board.length; i++) {
    if (board[i] === "X") cnt++;

    if (board[i] === "." || i === board.length - 1) {
      if (cnt % 2 !== 0) {
        answer = -1;
        break;
      }

      answer += "AAAA".repeat(cnt / 4);
      cnt = cnt % 4;
      answer += "BB".repeat(cnt / 2);
      cnt = 0;
    }

    if (board[i] === ".") answer += ".";
  }

  console.log(answer);
}

solution();
