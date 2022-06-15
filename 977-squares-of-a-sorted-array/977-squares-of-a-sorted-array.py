class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ls=[]
        for num in nums:
            ls.append(num**2)
        return sorted(ls)