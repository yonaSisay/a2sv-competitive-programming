class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict_ = {}
        
        for i,val in enumerate(numbers):
            dif = target-numbers[i]
            if dif in dict_: 
                return [min(i+1,dict_[dif]+1),max(i+1,dict_[dif]+1)]
            dict_[numbers[i]] = i