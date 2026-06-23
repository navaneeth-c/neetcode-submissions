func characterReplacement(s string, k int) int {
	var count [26]int

	l, maxLength, maxF := 0, 0, 0

	for r := 0; r < len(s); r++ {
		cIndex := s[r] - 'A'
		count[cIndex]++
		maxF = max(maxF, count[cIndex])

		if (r - l + 1) - maxF > k {
			count[s[l] - 'A']--					
			l++
		}
		maxLength = max(maxLength, r - l + 1)
	}
	return maxLength
}
