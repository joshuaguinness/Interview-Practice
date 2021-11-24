class MyHashMap:

    def __init__(self):
        self.map = []
        

    def put(self, key: int, value: int) -> None:
        for i, item in enumerate(self.map):
            if key == item[0]:
                self.map[i] = (key, value)
                return;
            
        self.map.append((key, value))

    def get(self, key: int) -> int:
        for i, item in enumerate(self.map):
            if key == item[0]:
                return item[1]
            
        return -1

    def remove(self, key: int) -> None:
        for i, item in enumerate(self.map):
            if key == item[0]:
                self.map.remove(item)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)