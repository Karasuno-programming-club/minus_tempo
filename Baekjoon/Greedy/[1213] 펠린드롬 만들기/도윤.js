const INPUT = require("fs")
//   .readFileSync("/dev/stdin")
  .readFileSync("../../../input.txt")
  .toString()
  .trim()
  .split("");

//뒤집어도 동일한 문자열
function solution() {

    const inputs = INPUT;
    inputs.sort();

    let result = '';
    let count = 0;
    let oddStr = '';

    for (let i = 0; i < inputs.length; i++) {
        count++

        if(inputs[i] != inputs[i+1]) {
            if(count % 2 !== 0) oddStr = inputs[i];
            
            result += inputs[i].repeat(count/2) 
            count = 0
        }
        
    }

    result = result + oddStr + result.split("").reverse().join("");

    if(result.length === inputs.length) {
        console.log(result);
    } else {
        console.log("I'm Sorry Hansoo")
    }
    

}

solution();