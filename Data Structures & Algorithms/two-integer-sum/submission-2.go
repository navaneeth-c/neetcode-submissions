func twoSum(nums []int, target int) []int {
    
	// create a map with key is the number and the value is the index for easy return
	// so this is a slice? Basically the size is not yet fixed, it should be able to expand in memory, wehereas arrays can not expand in memory dynamically. thats the dff between slice and array? 
	seen := make(map[int]int)
	
	for i, val:= range nums {
		if idx, exist := seen[target-val]; exist {
			return []int{idx, i}
		}
		seen[val] = i
	}
	return nil
}
