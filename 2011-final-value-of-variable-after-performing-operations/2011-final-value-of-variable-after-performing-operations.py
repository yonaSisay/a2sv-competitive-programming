class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x =0
        for elm in operations:
            if elm == "--X" or elm == "X--":
                x -=1
            elif elm =="++X" or elm =="X++":
                x +=1
        return x