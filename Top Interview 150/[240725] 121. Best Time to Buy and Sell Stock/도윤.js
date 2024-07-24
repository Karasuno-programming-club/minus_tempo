/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let minPrice = prices[0];
    let profit = 0;

    for (let i = 1; i < prices.length; i++) {
        if (minPrice > prices[i]) {
            minPrice = prices[i];
            continue;
        }

        if (profit < prices[i] - minPrice) {
            profit = prices[i] - minPrice;
        }
    }

    return profit
};

maxProfit([7,1,5,3,6,4]);

//단일 패스법