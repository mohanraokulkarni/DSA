class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        mul=m*n
        len_org=len(original)
        new_ls=[]

        if mul!=len_org:
            return new_ls
        

        for i in range(0,len_org,n):
            ls=original[i:i+n]
            new_ls.append(ls.copy())
        
        return new_ls
        