class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        try:
            n = float(s)
            return True
        except ValueError:
            return False
