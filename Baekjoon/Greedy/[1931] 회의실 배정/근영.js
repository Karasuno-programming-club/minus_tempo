const INPUT = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

function solution() {
  const N = Number(INPUT[0]);

  // 1) 2차원 배열로 만듦
  const times = [];

  for (let i = 1; i <= N; i++) {
    const time = INPUT[i].split(" ").map(Number);
    times.push(time);
  }

  // 2) 회의 종료 시간 기준 오름차순으로 정렬
  times.sort((a, b) => {
    if (a[1] === b[1]) {
      return a[0] - b[0];
    }

    return a[1] - b[1];
  });

  // 3) 최대 몇 개까지 들어가는지 카운트
  let count = 0;
  let cur = [0, 0]; // 마지막 회의의 시작, 끝 시각

  for (let i = 0; i < N; i++) {
    const [start, end] = times[i];
    if (start < cur[1]) {
      continue;
    } else {
      count++;
      cur = [start, end];
    }
  }
  console.log(count);
}

solution();
