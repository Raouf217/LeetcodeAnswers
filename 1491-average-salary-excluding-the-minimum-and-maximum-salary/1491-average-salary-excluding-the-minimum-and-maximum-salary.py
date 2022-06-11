class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        salary.pop(salary.index(min(salary)))
        salary.pop(salary.index(max(salary)))
        return float(sum(salary))/len(salary)