class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
#         for i in nums:
#             nums.insert(len(nums),0)
#             nums.pop(nums.index(0))
        for j in range(nums.count(0)):
              nums.remove(0)
              nums.append(0)