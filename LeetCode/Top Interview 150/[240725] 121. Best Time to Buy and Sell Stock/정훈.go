func maxProfit(prices []int) int {
    minPrice := prices[0]
    maxProfit := 0
    for _, p := range prices {
        minPrice = min(minPrice, p)
        maxProfit = max(maxProfit, p - minPrice)
    }
    return maxProfit
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func min(a, b int) int {
    if a > b {
        return b
    }
    return a
}
