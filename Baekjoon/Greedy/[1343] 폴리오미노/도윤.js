const INPUT = require("fs")
//   .readFileSync("/dev/stdin")
  .readFileSync("../../../input.txt")
  .toString()
  .trim();

function solution() {
    let input = INPUT;

    input = input.replace(/XXXX/g, "AAAA");
    input = input.replace(/XX/g, "BB");

    for(let s of input) {
        if(s === "X") input = -1;
    }

    console.log(input);
}

solution();