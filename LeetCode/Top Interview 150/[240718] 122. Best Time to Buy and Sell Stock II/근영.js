var maxProfit = function(prices) {
    let buy = prices[0];
    let profit = 0;

    for(let i = 0; i < prices.length; i++){
        if(buy < prices[i]){
            profit += prices[i] - buy;
        }
        buy = prices[i]
    }
    return profit
};

// 1과 다르게 그리디로 접근하는 solution
