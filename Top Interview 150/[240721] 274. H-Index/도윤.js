/**
 * @param {number[]} citations
 * @return {number}
 */
var hIndex = function(citations) {

    citations.sort((a,b) => b - a);
    for (let i = 0; i < citations.length; i++) {
        if(citations[i] < i + 1) {
            return i 
        }
    }

   return citations.length
};

console.log(hIndex([100]))

/**
 * 인용 횟수가 3번 이상인 논문이 3개 
 * hInde는 3
 */