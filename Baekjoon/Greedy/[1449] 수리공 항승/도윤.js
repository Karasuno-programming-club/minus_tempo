const INPUT = require("fs")
//   .readFileSync("/dev/stdin")
  .readFileSync("../../../input.txt")
  .toString()
  .trim()
  .split("\n");


  function solution() {
    const [holeCnt, tapeLength] = INPUT[0].split(" ").map(Number);

    if(tapeLength === 1) {
      console.log(holeCnt);
      return;
    }

    const holePlace = INPUT[1].split(" ").map(Number).sort((a,b) => a - b);    

    let useTapeCnt = 1;
    let currentTarget = holePlace[0]

    for (let i = 1; i < holeCnt; i++) {

      if (holePlace[i] > currentTarget + tapeLength - 1) {
        useTapeCnt++;
        currentTarget = holePlace[i];
      }
    }
        
    console.log(useTapeCnt);
  }

solution();





