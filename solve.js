// 백준 js 문제풀이를 위한 컨벤션
// - 제출후엔 꼭 원래 상태로 만들어주세요
// - .readFileSync("/dev/stdin") 로 변경 후 제출해야 합니다.

// 사용 방법
// 1) input.txt에 문제 관련 테스트 케이스를 입력한다.
// 2) convention.js 에서 해당 파일을 fs를 통해 불러와 사용한다.
// 2-1) input 타입이 number면 뒤에 .map(Number)를 붙여 숫자로 변환한다.
// 2-2) split(' ') - 한 줄 입력 받을 때 / spilt('\n') - 여러 줄 입력 받을 때

const INPUT = require("fs")
  .readFileSync("input.txt")
  .toString()
  .trim()
  .split("\n")
  // .split(' ')
  .map(Number);

function solution() {
  /**
   * 문제는 여기에 풉니다
   */
}

solution();
