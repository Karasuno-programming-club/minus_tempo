const INPUT = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt")
  .toString()
  .trim()
  .split("\n");

function solution() {
  T = Number(INPUT[0]);
  first = INPUT[1];
  let answer = 0;

  for (let i = 2; i < T + 1; i++) {
    const word = INPUT[i];
    let compare = first;

    let cnt = 0;

    for (w of word) {
      if (compare.indexOf(w) > -1) {
        compare = compare.replace(w, "");
      } else {
        cnt++;
      }
    }

    if (cnt < 2 && compare.length < 2) {
      answer++;
    }
  }
  console.log(answer);
}

solution();
