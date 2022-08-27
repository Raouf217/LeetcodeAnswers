class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = [str(integer) for integer in digits]
        a_string = "".join(s)
        res = int(a_string) + 1 
        return list(str(res))
        
        
