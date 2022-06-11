# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # We use left = 0, right = n and and check if the mid = (left + right) // 2 is bad that means
    # first bad is at left-er side so updating right = mid but if the mid is not bad that means
    # the first bad is at right-er side so we update our left = mid + 1; mid + 1 because we've
    # already seen the mid now we want to start from the next that's why +1. And eventually
    # while loop exhausts and we find our first bad version at left pointer.
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left