class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x,y):
            return int(x + y) - int(y + x)

        nums = list(map(str, nums))
        nums.sort(key = cmp_to_key(compare), reverse = True)

        return str(int("".join(nums)))