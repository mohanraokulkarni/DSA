class Solution:
    def fib(self, n: int) -> int:
        d={0:0,1:1}
        def fibn(n):
            if n in d:
                return d[n]
            k=fibn(n-1)
            d[n-1]=k
            j=fibn(n-2)

            return k + j
       
        res=fibn(n)
        
        return res
            
        