class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        result = 0
        for B in range(len(columnTitle)):
            result *= 26
            result += ord(columnTitle[B]) - ord('A') + 1

        return result