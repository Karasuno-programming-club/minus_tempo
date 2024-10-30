const INPUT = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt")
  .toString()
  .trim()
  .split("\n");

function solution() {
  const [N, M] = INPUT[0].split(" ").map(Number)
  const names = [];
  const values = [];

 for(let i = 1; i <= N; i++){
  const [name, value] = INPUT[i].split(" ")
  names.push(name);
  values.push(Number(value));
 }

 for(let i = N+1; i <= N+M; i++){
  const cur = Number(INPUT[i]);
  let start = 0;
  let end = N - 1;

  while(start < end){
    const mid = parseInt((start + end) / 2);

    if(cur <= values[mid]){
      end = mid;
    } else {
      start = mid + 1;
    }
  }

  console.log(names[start])
 }
}

solution();

// 파이썬 코드 js로 옮겼는데 시간초과남
// 근데 방법은 맞아서 그냥 넘어감