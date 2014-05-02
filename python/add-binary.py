class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string

    def addBinary(self, a, b):
        res_dec = int(a, 2)+int(b, 2)
        return bin(res_dec)[2:]
