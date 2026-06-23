func isValid(s string) bool {
    // when see open para put it in stack and vice versa when seen a closed bracket and compare it with the map of what to expect
	mapping := map[byte]byte{'}':'{', ']':'[', ')':'('}
	stack := []byte{}

	for i:=0; i<len(s); i++{
		c := s[i]
		if val, ok := mapping[c]; ok {
			if len(stack) == 0 {
				return false
			}

			top := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			if top != val {
				return false
			}
		} else {
			stack = append(stack, c)
		}
	}
	return len(stack) == 0

}
