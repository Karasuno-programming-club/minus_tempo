const INPUT = require("fs")
//   .readFileSync("/dev/stdin")
  .readFileSync("../../../input.txt")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

function solution() {
   
    const N = INPUT[0];
    const inputs = INPUT.slice(1);
    inputs.sort((a,b) => b - a);

    let max = inputs[0];

    for(let i = 1; i < inputs.length; i++ ) { 
        const cur = inputs[i] * (i + 1);
        if(max < cur) max = cur;
    }
    

    console.log(max);
}

solution();