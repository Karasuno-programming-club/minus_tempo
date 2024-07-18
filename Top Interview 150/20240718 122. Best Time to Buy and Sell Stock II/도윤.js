/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let totalProfit = 0;
    for (let i = 1; i < prices.length; i++) {
        if (prices[i] > prices[i - 1]) {
            totalProfit += prices[i] - prices[i - 1];
        }
    }
    return totalProfit;
};

maxProfit([1,2,3,4,5]);

/**
 * 현재값과 다음값의 차이값이 양수 일 경우 매수 매도 시 이익이 발생한다
 * Array[i] - Array[i-1] > 0 을 충족하면, 이익이 발생한다.
 */