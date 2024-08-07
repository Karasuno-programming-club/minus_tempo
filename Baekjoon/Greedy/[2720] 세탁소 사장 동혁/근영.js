const INPUT = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

function solution() {
  const n = INPUT[0];
  const arr = INPUT.slice(1);
  let answer = "";
  let cost = [25, 10, 5, 1];

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < 4; j++) {
      answer += Math.floor(arr[i] / cost[j]) + " ";
      arr[i] %= cost[j];
    }
    answer += "\n";
  }

  console.log(answer);
}

solution();
