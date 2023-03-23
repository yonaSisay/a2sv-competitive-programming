class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.deque = Deque()   
        self.mapp = defaultdict(int)     

    def consec(self, num: int) -> bool:
        self.deque.append(num)       
        self.mapp[num] += 1

        if len(self.deque) > self.k:
            temp = self.deque.popleft()
            self.mapp[temp] -= 1 
            if self.mapp[temp] == 0:
                del self.mapp[temp]
        
        if len(self.deque) == self.k and self.mapp[self.value] == self.k:
            return True
        else:
            return False


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)