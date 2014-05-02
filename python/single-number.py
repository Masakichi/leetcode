class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        A.sort()
        if len(A)==1: return A[0]
        for x in range(0,len(A),2):
            try:
                if A[x] != A[x+1]:
                    return A[x]
            except:
                return A[x]
