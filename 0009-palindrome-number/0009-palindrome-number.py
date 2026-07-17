class Solution(object):
    def isPalindrome(self, x):
        y = str(x)
        if y[::-1] == y:
            return True
        else:
            return False
        