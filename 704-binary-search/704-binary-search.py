class Solution(object):
    def binary(self,nums, low, high,target):
        if high >=low:
            mid = (high + low) // 2
 
            # If element is present at the middle itself
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return self.binary(nums, low, mid - 1, target)

            # Else the element can only be present in right subarray
            else:
                return self.binary(nums, mid + 1, high, target)

        else:
            return -1
    
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
#         x =  self.binary(nums,0,len(nums)-1,target)
#         return x
       
        if target not in nums : return -1
        return nums.index(target)
    