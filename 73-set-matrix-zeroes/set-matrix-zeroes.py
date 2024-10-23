class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        row=[]
        col=[]

        n_rows=len(matrix)
        n_cols=len(matrix[0])

        for i in range(n_rows):
            for j in range(n_cols):
                if matrix[i][j]==0:
                    row.append(i)
                    col.append(j)
        
        for i in range(n_rows):
            for j in range(n_cols):
                if (i in row) or (j in col):
                    matrix[i][j]=0
        