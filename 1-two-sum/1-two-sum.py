class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # values = {}
        # for idx, value in enumerate(nums):
        #     if target - value in values:
        #         return [values[target - value], idx]
        #     else:
        #         values[value] = idx
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]