class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
            
        values = {} 
        for idx, value in enumerate(numbers):
            if target - value in values:
                return [values[target - value]+1, idx+1]
            values[value] = idx