const INPUT = require("fs")
  .readFileSync("/dev/stdin")
  // .readFileSync("../../../input.txt")
  .toString()
  .trim()
  .split("\n")
  // .split(' ')
  .map(Number);


const coins = [25, 10, 5, 1];


function solution() {
  let answer = '';
  const inputs = INPUT.slice(1);

  for (let input of inputs) {    
    for (let coin of coins) {
      answer += Math.floor(input / coin) + ' ';
      input %= coin;
    }

    answer = answer.trim() + "\n";
  }

  console.log(answer);
}

solution();