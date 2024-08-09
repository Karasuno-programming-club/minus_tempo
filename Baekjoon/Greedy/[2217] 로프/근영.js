const INPUT = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  // .split(' ')
  .map(Number);

function solution() {
  const N = INPUT[0];
  const ropes = INPUT.slice(1).sort((a, b) => a - b);
  let max = 0;

  for (let i = 0; i < N; i++) {
    max = Math.max(max, ropes[i] * (N - i));
  }

  console.log(max);
}

solution();
