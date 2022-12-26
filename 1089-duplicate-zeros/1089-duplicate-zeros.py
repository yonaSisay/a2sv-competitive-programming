class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        first i should cop
        the problem is i have to add the value if t
        """
        copy =[]
        l=0
        for i in range(len(arr)):
            if arr[i]==0:
                copy.append(0)
                copy.append(0)
            else:
                copy.append(arr[i])
        for i in range(len(arr)):
            arr[i] = copy[i]
        