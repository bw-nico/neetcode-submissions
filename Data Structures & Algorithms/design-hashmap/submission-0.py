class MyHashMap:

    def __init__(self):
        self.hashmap = []
        

    def put(self, key: int, value: int) -> None:
        append = True
        for idx, pair in enumerate(self.hashmap):
            if pair[0] == key:
                self.hashmap[idx][1] = value
                append = False
        if append:
            self.hashmap.append([key,value])
        

    def get(self, key: int) -> int:
        for each in self.hashmap:
            if key == each[0]:
                return each[1]
        return -1
        
        
    def remove(self, key: int) -> None:
        for idx, pair in enumerate(self.hashmap):
            if pair[0] == key:
                self.hashmap.pop(idx)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)