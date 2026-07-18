class Solution(object):
    def scoreOfString(self, s):
        suum = 0
        for i in range(len(s)-1):
            suum += abs(ord(s[i]) - ord(s[i+1]))
        return suum
        