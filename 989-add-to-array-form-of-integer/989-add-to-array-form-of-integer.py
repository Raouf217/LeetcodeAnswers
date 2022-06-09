class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        z = [str(x) for x in num]
        s=""
        s= s.join(z)
        sum = int(s) + k
        return list(str(sum))