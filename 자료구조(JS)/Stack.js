// Push : O(1)
// Pop : O(1)
// Top : O(1)
// Empty : O(1) - 스택이 비어 있는지 확인(boolean)

// head : 남아있는 원소 중 가장 마지막에 들어 온 데이터를 가리키는 포인터

let stack = [];

stack.push(5);
stack.push(2);
stack.push(3);
stack.push(7);
stack.pop();
stack.push(1);
stack.push(4);
stack.pop();

let reversed = stack.slice().reverse();
console.log(reversed); // 최상단 원소부터 출력 [ 1, 3, 2, 5 ]
console.log(stack); // [ 5, 2, 3, 1 ]
