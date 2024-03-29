class Solution(object):
    def minOperations(self, nums, x):
        target = sum(nums) - x
        if target == 0:
            return len(nums)
        if target < 0:
            return -1
        l, r, window = 0, 0, 0
        max_len = -1
        while r < len(nums):
            window += nums[r]
            r += 1
            while window >= target:
                if (window == target):
                    max_len = max(max_len, r - l)
                window -= nums[l]
                l += 1
        return -1 if max_len == -1 else len(nums) - max_len