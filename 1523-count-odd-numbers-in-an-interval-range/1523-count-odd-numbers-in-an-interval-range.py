class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
#         if(high%2 == 1):
#             high += 1
            
#         return high//2-low//2
        return [((high-low)//2)+1, (high-low)//2][high%2==0 and low%2==0]