// https://leetcode.com/problems/h-index/description/?envType=study-plan-v2&envId=top-interview-150

var hIndex = function(citations) {
    let hIdx = 0;
    let length = citations.length

    citations.sort((a,b) => a - b);

    for(let i = 1; i <= length; i++){
        if(citations[length - i] >= i){
            hIdx++;
        }
    }

    return hIdx 
};

// time : O(NLogN)
// space : O(1)