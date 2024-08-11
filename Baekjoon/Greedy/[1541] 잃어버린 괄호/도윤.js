const INPUT = require("fs")
//   .readFileSync("/dev/stdin")
  .readFileSync("../../../input.txt")
  .toString()
  .trim();


function solution() {
    const inputs = INPUT.split("-");
    
    
    // 마이너스가 없는 경우
    if(inputs.length === 1) {
        console.log(inputs[0].split("+").reduce((acc,curr) => acc + Number(curr), 0));
        return 0;
    }


    let sum = 0;
    for (let i = 0; i < inputs.length; i++) {

        inputs[i] = inputs[i].split("+").reduce((acc,curr) => acc + Number(curr), 0);
        
        if(i === 0) {
            sum += inputs[i];
        } else {
            sum -= inputs[i]
        }

    }

    console.log(sum);

}

solution();





