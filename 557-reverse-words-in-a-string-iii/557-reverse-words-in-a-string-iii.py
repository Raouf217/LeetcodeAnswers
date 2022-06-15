class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        for i, val in enumerate(s):
            s[i] = val[::-1]
            
        q=" "
        return q.join(s)