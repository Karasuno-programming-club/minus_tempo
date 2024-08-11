let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

let data = input[0];
let arr = data.split('-');
let answer = 0;

for(let i = 0; i < arr.length; i++){
    let cur = arr[i].split('+').map(Number).reduce((a, b) => a + b);
    if(i === 0) answer += cur;
    else answer -= cur;
}

console.log(answer)

// 예전에 풀었던 문제네요 ~