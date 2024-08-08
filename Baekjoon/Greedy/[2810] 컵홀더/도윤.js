const INPUT = require("fs")
//   .readFileSync("/dev/stdin")
  .readFileSync("../../../input.txt")
  .toString()
  .trim()
  .split("\n");

function solution() {


    let count = Number(INPUT[0]);
    let input = INPUT[1];

    input = input.replace(/LL/g, "*LL*");
    input = input.replace(/S/g, "*S*");
    input = input.replace(/\*\*/g, "*");

    let result = 0;

    for (let i = 0; i < input.length; i++) {
        if(input[i] === '*') result++;
    }

    console.log(result > count ? count : result);
}

solution();