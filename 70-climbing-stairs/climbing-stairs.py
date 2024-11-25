class Solution:
    def climbStairs(self, n: int) -> int:
        memo={}
        def move(x):
            if x>n:
                return 0
            if x == n:
                return 1
            if x in memo:
                return memo[x]
            memo[x]=move(x+1) + move(x+2)

            return memo[x]
        return move(0)