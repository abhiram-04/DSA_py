class Solution(object):
    def mostWordsFound(self, sentences):
        con = 0
        for i in range(len(sentences)):
            arc = sentences[i].split()
            con = max(con,len(arc))
        return con
            
        