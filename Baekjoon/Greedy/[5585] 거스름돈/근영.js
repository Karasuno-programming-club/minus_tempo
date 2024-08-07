const INPUT = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

function solution() {
  let count = 0;
  let ret = 1000 - INPUT[0];
  const arr = [500, 100, 50, 10, 5, 1];

  for (let i = 0; i < 6; i++) {
    let c = Math.floor(ret / arr[i]);
    if (c > 0) {
      count += c;
      ret -= arr[i] * c;
    }
  }

  console.log(count);
}

solution();
