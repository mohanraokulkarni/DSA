class Solution:
    def longestPalindrome(self, s: str) -> str:
        l=len(s)
        def palindrom(st):
            if st==st[::-1]:
                return True
            return False
        max_len=2
        pal_str=str()
        for i in range(0,l):
            for j in range(i,l):
                sub_s=s[i:j+1]
                len_sub=len(sub_s)
                if palindrom(sub_s):
                    if max_len<=len_sub:
                        max_len=len_sub
                        pal_str=sub_s
        if len(pal_str)==0:
            return s[0]
        return pal_str