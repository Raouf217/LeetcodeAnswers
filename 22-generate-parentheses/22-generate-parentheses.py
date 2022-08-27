from functools import cache
class Solution:
    @cache
    def generateParenthesis(self, n: int, memo = None) -> List[str]:
        if n == 0 :
            return [ "" ]
        s=[]
        for i in range(0,n):
            for x in self.generateParenthesis(i):
                try:
                    for y in self.generateParenthesis(n-i-1):
                        s= s+[x + "(" + y + ")"]
                except:pass
        return s