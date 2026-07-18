class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        suum = 0
        for i in range(len(jewels)):
            for j in range(len(stones)):
                if jewels[i] == stones[j]:
                    suum+=1
        return suum