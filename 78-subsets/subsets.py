class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def subset(ls,cur,index):
            if index>=len(ls):
                subset_lis.append(cur.copy())
                return 
            
            subset(ls,cur,index+1)#with out the number 
            
            cur.append(ls[index])
            
            subset(ls,cur,index+1)#with the number 
            
            cur.pop()  # backtracking to the previous nod 
        
        ls=nums
        subset_lis=[]
        subset(ls,[],0)
        return subset_lis
        