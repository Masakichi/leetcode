class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        l = [x.lower() for x in s if x.isalnum()]
        if l:
            result = True if l == list(reversed(l)) else False
            return result
        else:
            return True
