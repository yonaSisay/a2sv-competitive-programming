class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times        

        mapp = defaultdict(int)
        tracker = self.persons[0]
        self.score = []

        for person in self.persons:
            mapp[person] += 1
            if mapp[tracker] <= mapp[person]:
                tracker = person
            self.score.append(tracker)
       
    def q(self, t: int) -> int:

        high = len(self.times) - 1
        low = 0

        while low <= high:
            mid = low + (high - low) // 2

            if self.times[mid] > t:
                high = mid - 1
            else:
                low = mid + 1
        
        return self.score[high]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)