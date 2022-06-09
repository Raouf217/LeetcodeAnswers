class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = int(a, base=2)
        b = int(b, base=2)
        c= a+b
        c = bin(c)[2:]
        return c