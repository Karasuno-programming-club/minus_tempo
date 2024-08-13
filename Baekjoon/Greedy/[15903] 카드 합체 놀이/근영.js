// 시간 초과 풀이 ㅠ
const INPUT = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

function solution() {
  const [n, m] = INPUT[0].split(" ").map(Number);
  const cards = INPUT[1].split(" ").map(Number);

  // 1) 오름차순 sort
  cards.sort((a, b) => a - b);

  let count = m;
  while (count > 0) {
    // 2) 카드 합체
    const total = cards[0] + cards[1];
    cards[0] = total;
    cards[1] = total;

    // 3) 다시 sort
    cards.sort((a, b) => a - b);
    count--;
  }
  // 4) 합 구하기
  const answer = cards.reduce((acc, cur) => BigInt(acc) + BigInt(cur));
  console.log(answer.toString());
}

solution();
