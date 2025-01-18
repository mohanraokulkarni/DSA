class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1=len(text1)
        len2=len(text2)
        grid=[[0 for _ in range(len2+1)] for _ in range(len1+1)]

        for i in range(1,len1+1):
            for j in range(1,len2+1):
                if text1[i-1] != text2[j-1]:
                    grid[i][j]= max(grid[i-1][j], grid[i][j-1])
                else:
                    # if same
                    grid[i][j]=1+grid[i-1][j-1]
        return grid[len1][len2]



