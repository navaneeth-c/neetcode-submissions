class TimeMap:

    def __init__(self):
        # key : string key
        # value: list of tuples. eg ([(timestamp, value), ....])
        # {key<string>: (int, string)tuple.}
        # need to see how we can represent these ds in golang. 
        # make(map[string][](int, string))?

        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store: 
            self.store[key] = []
        
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.store: 
            return res
        
        values = self.store[key]
        l, r = 0, len(values) - 1
        # we need to do <= because, we are looking for a shrink method. so answer might collide? 
        # still am not clear. we saw so many bs examples, adn wnna solidify pattern
        while l <= r:
            mid = l + ((r - l) // 2)
            if values[mid][0] <= timestamp: 
                res = values[mid][1]
                l = mid + 1
            else: 
                r = mid - 1
        
        return res
