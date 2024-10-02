class Solution:
    def longestValidParentheses(self, s: str) -> int:
        last_not_valid=-1

        stack=[]
        l=len(s)
        max_length=0

        for i in range(0,l):
            if s[i]=="(":
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                    if stack:
                        max_length=max(max_length,i-stack[-1])
                    else:
                        max_length=max(max_length,i-last_not_valid)
                else:
                    last_not_valid=i
        return max_length


        