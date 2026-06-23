func longestConsecutive(nums []int) int {
	// 1. Add elements to a set
	// 2. iterate thropugh the slice
			// check if the number is starting of sequence
			// 		counter to increment till next element in set. 
			// if not continue
	// return counter
	max_count := 0
	seen := make(map[int]struct{})
	for _, val := range nums {
		seen[val] = struct{}{}
	}

	for _, val:= range nums{
		if _, exists:=seen[val-1]; exists {
			continue
		}
		current_max := 1
		curr_val := val
		for {
			if _,exists:=seen[curr_val+1]; !exists {
				break
			}
			current_max++
			curr_val++
		}
		max_count = max(max_count, current_max)
	}
	return max_count
}
