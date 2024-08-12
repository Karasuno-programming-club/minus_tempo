const INPUT = require("fs")
//   .readFileSync("/dev/stdin")
  .readFileSync("../../../input.txt")
  .toString()
  .trim()
  .split("\n");


function solution() {
    const [count, ...times] = INPUT;
    times.sort((a,b) => {
        if(Number(a.split(" ")[0]) - Number(b.split(" ")[0]) === 0) {
            return Number(a.split(" ")[1]) - Number(b.split(" ")[1]) ;
        }
        return Number(a.split(" ")[0]) - Number(b.split(" ")[0]);
    });

    let [ startTarget, endTarget ] = times[0].split(" ").map(Number);
    let result = 1;

    for(let i = 1; i < times.length; i++) {

        const [ startTime, endTime ] = times[i].split(" ").map(Number);
        const interval = startTime - startTarget;
        
        // 간격 기준으로 한다
        if(endTarget - startTarget > (endTime - startTime) + (interval)) {
            startTarget = startTime;
            endTarget = endTime;
        } else if (endTarget <= startTime) {
            result++;
            startTarget = startTime;
            endTarget = endTime; 
        }
    }
   
    console.log(result);
    
}

solution();





