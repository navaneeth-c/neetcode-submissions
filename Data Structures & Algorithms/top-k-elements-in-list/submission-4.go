func topKFrequent(nums []int, k int) []int {
	count := make(map[int]int)
	for _, num := range nums {
		count[num]++
	}

	buckets := make([][]int, len(nums)+1)
	for val, freq := range count {
		buckets[freq] = append(buckets[freq], val)
	}
	
	var res []int
	for i:= len(buckets)-1; i>0; i-- {
		if buckets[i] != nil {
			res = append(res, buckets[i]...)
		}
		if len(res) == k {
			break
		}
	}
	return res
}
