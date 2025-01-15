class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        l=[i for i in range(1,n+1)]

        from itertools import combinations

        c=list(combinations(l,k))

        return c

        