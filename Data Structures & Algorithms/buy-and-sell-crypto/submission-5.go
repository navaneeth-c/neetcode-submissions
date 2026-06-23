func maxProfit(prices []int) int {
	if len(prices) < 2 {
		return 0
	}
	max_profit := 0
	l := 0
	r := 1
	for l < r && r < len(prices){
		if prices[l] > prices[r] {
			l = r
		} else {
			curr := prices[r] - prices[l]
			max_profit = max(max_profit, curr)
		}
		r++
	}
	return max_profit
}


