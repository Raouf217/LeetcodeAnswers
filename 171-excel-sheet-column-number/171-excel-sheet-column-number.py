class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        result = 0
        for i in range(len(columnTitle)):
            result *= 26
            result += ord(columnTitle[i]) - ord('A') + 1

        return result