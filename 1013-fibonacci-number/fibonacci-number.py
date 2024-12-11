class Solution:
    def fib(self, n: int) -> int:
        d={0:0,1:1}
        def fibn(n):
            if n in d:
                return d[n]
            return fibn(n-1)+fibn(n-2)
        res=fibn(n)
        return res
            
        