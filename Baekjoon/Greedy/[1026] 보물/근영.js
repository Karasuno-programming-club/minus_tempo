const INPUT = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

function solution() {
  const N = Number(INPUT[0]);
  const arrA = INPUT[1].split(" ").map(Number);
  const arrB = INPUT[2].split(" ").map(Number);

  const sortedA = arrA.sort((a, b) => a - b);
  const sortedB = arrB.sort((a, b) => b - a);
  let answer = 0;

  for (let i = 0; i < N; i++) {
    answer += sortedA[i] * sortedB[i];
  }

  console.log(answer);
}

solution();
