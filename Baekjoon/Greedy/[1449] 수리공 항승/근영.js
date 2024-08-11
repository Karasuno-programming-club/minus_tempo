function solution() {
    const [N, L] = INPUT[0].split(" ").map(Number);
    const holes = INPUT[1].split(" ").map(Number).sort((a, b) => a - b);
    // 문제에서 sort되어 있다고 명시되지 않음 !!
  
    let tapeStart = 0;
    let tapeEnd = 0;
    let count = 0;
  
    for(let i = 0; i < N; i++){
      let start = holes[i] - 0.5;
      let end = holes[i] + 0.5;
  
      if(tapeStart <= start && tapeEnd >= end){
        continue;
      } else {
        count++;
        tapeStart = start;
        tapeEnd = start + L;
      }
    }
  
    console.log(count)
  }
  
  solution();