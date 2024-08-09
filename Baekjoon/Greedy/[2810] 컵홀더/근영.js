const INPUT = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

function solution() {
  const N = Number(INPUT[0]);
  const arr = INPUT[1].split("");

  let cup = 1; // 맨 처음에 컵홀더가 하나 있음

  for (let i = 0; i < N; i++) {
    if (arr[i] === "L") {
      i++;
    }
    cup++;
  }
  console.log(Math.min(N, cup));
}

solution();
