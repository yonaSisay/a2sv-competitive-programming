class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num_reverse = str(x)[::-1]
        
        if str(x) == num_reverse:
            return True
        else:
            return False
        