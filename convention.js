// 백준 js 문제풀이를 위한 컨벤션
// 1) input.txt에 문제 관련 테스트 케이스를 입력한다.
// 2) convention.js 에서 해당 파일을 fs를 통해 불러와 사용한다.
// 2-1) input 타입이 number면 뒤에 .map(Number)를 붙여 숫자로 변환한다.

const INPUT = require("fs")
  .readFileSync("input.txt")
  .toString()
  .trim()
  .split("\n");
//.map(Number);

function solution() {
  console.log(INPUT);
  /**
   * 여기에 문제를 풉니다
   */
}

module.exports = solution;
