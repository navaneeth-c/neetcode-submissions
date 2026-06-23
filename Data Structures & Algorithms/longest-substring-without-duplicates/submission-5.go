func lengthOfLongestSubstring(s string) int {
	charSet := make(map[byte]bool)
	l:=0
	maxLen:=0

	for r:=0 ; r < len(s); r++ {
		for charSet[s[r]] {
			charSet[s[l]] = false
			l++
		}

		charSet[s[r]] = true
		maxLen = max(maxLen, r - l + 1)
	}
	return maxLen
}
