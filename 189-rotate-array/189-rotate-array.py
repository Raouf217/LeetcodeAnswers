class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # ls = []
        # while k:
        #     ls.append(nums[-1])
        #     nums.pop(-1)
        #     for i in nums: ls.append(i)
        # nums = ls
        n = len(nums)
        k = k % n
        nums[:] = nums[-k:] + nums[:-k]