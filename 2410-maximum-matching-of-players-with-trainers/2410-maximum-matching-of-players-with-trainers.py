class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        count = 0
        
        players.sort()
        trainers.sort()
        
        pl = 0
        tr = 0
        
        while pl < len(players) and tr < len(trainers):
            if players[pl] > trainers[tr]:
                tr += 1
            elif players[pl] <= trainers[tr]:
                tr += 1
                pl += 1
                count += 1
        return count