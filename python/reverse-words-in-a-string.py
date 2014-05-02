class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        l = s.split(' ')
        l.reserve()
        return l.join(' ')
