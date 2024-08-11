const INPUT = require("fs")
.readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

function solution() {
  const T = Number(INPUT[0]);
  let answer = "";

  for(let i = 1; i < T * 2; i+=2){
    const day = Number(INPUT[i]);
    const arr = INPUT[i+1].split(" ").map(Number);
    let max = 0;
    let profit = 0;
    for(let i = day - 1; i >= 0; i--){
      if(arr[i] > max){
        max = arr[i];
      } else {
        profit += max - arr[i]
      }
    }
    answer += `${profit}\n`
  }
  console.log(answer);
}

solution();

// 거꾸로 진행하면서 이익 계산하기
// 를 어떻게 생각하냐고 ~~~~~~~~~~~~~