func maxArea(heights []int) int {
	if len(heights) < 2 {
		return 0
	}

	maxArea := 0
	l, r := 0, len(heights) - 1
	for l < r {
		area := (r - l) * min(heights[l], heights[r])
		maxArea = max(maxArea, area)
		if heights[l] <= heights[r] {
			l++
		} else {
			r--
		}
	}
	return maxArea
}
