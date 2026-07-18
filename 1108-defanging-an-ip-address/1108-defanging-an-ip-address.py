class Solution(object):
    def defangIPaddr(self, address):
        stri = ""
        for i in range(len(address)):
            if address[i] != ".":
                stri+=address[i]
            else:
                stri+="[.]"
        return stri


        