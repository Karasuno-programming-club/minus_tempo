const PriorityQueue = require('./index.js')

const INPUT = require("fs")
  .readFileSync("../../../input.txt")
  .toString()
  .trim()
  .split("\n")



function solution() {

    const queue = new PriorityQueue((a,b) => b - a);

    const [ count, changes ] = INPUT[0].split(" ").map(Number);
    const cards = INPUT[1].split(" ").map(Number);

    cards.forEach((value, index) => queue.enq(BigInt(value)));
    let changeCount = changes;



  
    while(changeCount > 0){


        const sum = BigInt(queue.deq()) + BigInt(queue.deq());
        queue.enq(sum);
        queue.enq(sum);
        changeCount--;
    } 

    
    let result = BigInt(0);
    queue.forEach((item,index) => {
      if(item) result = result + BigInt(item);
    })

    console.log(result.toString());

}

solution();

