const INPUT = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt")
  .toString()
  .trim()
  .split("\n");

function solution() {
  S = INPUT[0].split("")
  
  // 개수
  const init_1 = S.filter((v) => v === "1").length;
  const init_0 = S.length - init_1

  // 1은 앞에서부터 지운다
  let cnt = 0
  for(let i = 0; i < S.length; i++){
    if(cnt === init_1 / 2){
      break
    }
    if(S[i] === "1"){
      S[i] = "";
      cnt += 1;
    }
  }
  // 0은 뒤에서부터 지운다
  cnt = 0
  for(let i = S.length - 1; i >= 0; i--){
    if(cnt === init_0 / 2){
      break
    }
    if(S[i] === "0"){
      S[i] = "";
      cnt += 1;
    }
  }

  console.log(S.join(""))
}

solution();