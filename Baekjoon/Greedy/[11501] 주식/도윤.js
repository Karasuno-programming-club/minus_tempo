const INPUT = require("fs")
  .readFileSync("../../../input.txt")
  .toString()
  .trim()
  .split("\n")
//   .map(Number);


function solution() {

    // const testCaseCnt = Number(INPUT[0]);

    const tests = INPUT.slice(1);
    const result = [];


    for (let i = 0; i < tests.length; i=i+2) {
        const stocks = tests[i+1].split(" ").map(Number);


        let maxPrice = stocks[stocks.length - 1];
        let profit = 0;

        for (let k = stocks.length - 2; k >= 0 ; k--) {
            if (maxPrice < stocks[k]) {
                maxPrice = stocks[k];
            } else {
                profit += maxPrice - stocks[k] > 0 ? maxPrice - stocks[k] : 0;
            }
        }

        result.push(profit);

        
    }

    result.map((item, _) => console.log(item));

}

solution();