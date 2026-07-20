class Solution(object):
    def singleNumber(self, nums):
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num,0)+1
        for num in frequency:
            if frequency[num] == 1:
                return num
        