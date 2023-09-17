class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        salary.remove(min(salary))
        salary.remove(max(salary))
        return sum(salary)/len(salary)
        
p1=Solution()
print(p1.average([48000,59000,99000,13000,78000,45000,31000,17000,39000,37000,93000,77000,33000,28000,4000,54000,67000,6000,1000,11000]))

        
        
