class Solution:
    def helper(self, arr, l , r, p):
        # base case
        if l == r:
            if p:
                return [arr[l] ,0]
            else:
                return [0 , arr[l]]
        
        if p:
            right = self.helper(arr,l , r - 1, not p)
            right[0] += arr[r]
            left = self.helper(arr , l + 1, r, not p)
            left[0] += arr[l]
            
            if right[0] > left[0]:
                return right
            else:
                return left
        else:
            right = self.helper(arr,l , r - 1, not p)
            right[1] += arr[r]
            left = self.helper(arr , l + 1, r, not p)
            left[1] += arr[l]
            
            if right[1] > left[1]:
                return right
            else:
                return left
        
    def PredictTheWinner(self, nums: List[int]) -> bool:
        score = self.helper(nums, 0, len(nums) - 1, True)
        return score[0] >= score[1]