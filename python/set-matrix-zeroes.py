class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        all = []
        for x,y in enumerate(matrix):
            for k,v in enumerate(y):
                if v==0:
                    all.append(k)
                    matrix[x] = [0 for i in y]
        all = list(set(all))
        for z in all:
            for p,q in enumerate(matrix):
                matrix[p][z]=0
