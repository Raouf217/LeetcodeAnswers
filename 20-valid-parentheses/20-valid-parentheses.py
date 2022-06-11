class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = ["(", "[", "{", ")", "]", "}"]
        stack = []
        
        for element in s:
            if element in brackets[0:3]:
                stack.append(element)
            if element in brackets[3:]:
                if len(stack) == 0:
                    return False
                top_of_stack = stack.pop()
                if brackets.index(top_of_stack) != brackets.index(element) - 3:
                    return False
                
        if len(stack) == 0:
            return True
        else:
            return False