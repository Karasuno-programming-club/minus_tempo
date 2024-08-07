const INPUT = require("fs")
  .readFileSync("/dev/stdin")
//   .readFileSync("../../../input.txt")
  .toString()
  .trim()
  .split("\n")
  .map(Number);


const coins = [500, 100, 50, 10, 5, 1];


function solution() {
    let answer = 0;
    let input = 1000 - INPUT;

    for (let coin of coins) {
        answer += Math.floor(input / coin);
        input %= coin;
    }

    console.log(answer);
}

solution();