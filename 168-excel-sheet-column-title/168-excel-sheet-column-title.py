class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
       
    
        if columnNumber<0 :return ""
        n = columnNumber
        A = ord("A")
        res = []
        while n > 0:
            if n > 26:
                i = n % 26
                if i == 0:
                    res.append('Z')
                    n -= 26
                else:
                    res.append(chr(A + i - 1))
                n //= 26
            else:
                res.append(chr(A + n - 1))
                break
        res.reverse()
        return ''.join(res)