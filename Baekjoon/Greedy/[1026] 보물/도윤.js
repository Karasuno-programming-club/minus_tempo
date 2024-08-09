const INPUT = require("fs")
//   .readFileSync("/dev/stdin")
  .readFileSync("../../../input.txt")
  .toString()
  .trim()
  .split("\n");

function solution() {
    const N = Number(INPUT[0]);

    
    let A = INPUT[1].split(' ').map(Number);
    let B = INPUT[2].split(' ').map(Number);

    let resultMin = 0;

    // console.log(N);
    // console.log(A);
    // console.log(B);

    //B가 최대일 때 A는 최소여야한다
    A.sort((a,b) => a - b);
    B.sort((a,b) => b - a);

    for (let i = 0; i < N; i++ ) {
        resultMin += A[i] * B[i];
    }

    console.log(resultMin);


}

solution();