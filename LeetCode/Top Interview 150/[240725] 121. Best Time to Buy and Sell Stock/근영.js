// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan-v2&envId=top-interview-150

// brute force (O(N²))
var maxProfit = function(prices) {
    let answer = 0;

    for(let i = 0; i < prices.length; i++){
        let max = 0;
        for(let j = i+1; j < prices.length; j++){
            let profit = prices[j] - prices[i];
            if(profit > max){
                max = profit
            }
        }
        if(max > answer){
            answer = max;
        }
    }
    return answer;
};

//solution(O(N))
var maxProfit = function(prices) {
    let buy = prices[0];
    let profit = 0;
 
    for(let i = 0; i < prices.length; i++){
     if(prices[i] < buy){
         buy = prices[i]
     } else if(prices[i] - buy > profit){
         profit = prices[i] - buy;
     }
    }
    return profit
 };
