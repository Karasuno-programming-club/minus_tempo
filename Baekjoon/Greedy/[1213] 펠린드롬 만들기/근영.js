const INPUT = require("fs")
.readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

function solution() {
  const str = INPUT[0].split("").sort().join(""); // 알파벳 순 정렬
  const len = str.length;
  let answer = "";

  // 1) 문자 등장한 횟수 저장
  const obj = {};

  for(let i = 0; i < len; i++){
    obj[str[i]] = obj[str[i]] ? obj[str[i]] + 1 : 1;
  }

  // 2) 펠린드롬을 만들 수 있는지 체크
  // - 길이가 홀수 -> 1개의 문자가 홀수개 등장
  // - 길이가 짝수 -> 모든 문자가 짝수개 등장
  let odd = 0;
  let oddStr = '';
  Object.keys(obj).map((v) => {
    if(obj[v] % 2 !== 0) {
      odd++;
      oddStr = v;
    }
  })

  if(len % 2 !== 0 && odd !== 1){
    console.log("I'm Sorry Hansoo");
    return;
  }

  if(len % 2 === 0 && odd > 0){
    console.log("I'm Sorry Hansoo");
    return;
  }
  // 3) 펠린드롬 만들기
  // 홀수일 때
  let curStr = "";
  Object.keys(obj).map((v) => {
    curStr += v.repeat(Math.floor(obj[v] / 2));
  })
  answer = curStr;
  if(odd > 0) answer += oddStr;
  answer += curStr.split('').reverse().join('')

  console.log(answer)
}

solution();