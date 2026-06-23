func isPalindrome(s string) bool {
	if len(s) < 2 {
		return true
	}

	left, right := 0, len(s)-1

	for left < right {
		
		if !isAlnum(rune(s[left])) {
			left++
			continue
		}
		if !isAlnum(rune(s[right])) {
			right--
			continue
		}
		if unicode.ToLower(rune(s[left])) != unicode.ToLower(rune(s[right])) {
			return false
		} 
		left ++
		right --
	}
	return true

}
 func isAlnum(c rune) bool {
	return unicode.IsLetter(c) || unicode.IsDigit(c)
 }

