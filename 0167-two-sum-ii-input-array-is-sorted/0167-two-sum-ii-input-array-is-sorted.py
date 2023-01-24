class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0 
        right = len(numbers)-1
        ans = []
        while left<right:
            sum_ = numbers[left]+numbers[right]
            if sum_ > target:
                right -=1
            elif sum_ < target:
                left +=1
            elif sum_ == target:
                ans.append( left+1)
                ans.append(right+1)
                break
        return ans