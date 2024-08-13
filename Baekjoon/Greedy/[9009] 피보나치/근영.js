const INPUT = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  // .split(' ')
  .map(Number);

function solution() {
  const N = Number(INPUT[0]);
  const arr = INPUT.slice(1).map(Number);
  let answer = "";

  // 1)
  for(let i = 0; i < N; i++){
    let temp = arr[i];
    
    let curIdx = 2;
    let curVal = 1;
    const fibonacci = [0, 1];

    while(curVal <= temp){
      const next = fibonacci[curIdx - 2] + fibonacci[curIdx - 1];
      
      if(next > temp) break;

      fibonacci.push(next);
      curVal = next;
      curIdx++;
    }

    // 2)
    const tempLst = [];
    while(temp > 0){
      const last = fibonacci.pop();
      if(last <= temp){
        tempLst.push(last);
        temp -= last;
      }
    }

    tempLst.sort((a, b) => a - b);

    answer += `${tempLst.join(" ")}\n`
  }
  console.log(answer);
}

solution();