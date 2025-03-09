import numpy as np

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        array = np.array(nums)
        unique_elements, counts = np.unique(array, return_counts=True) 
        
        result = unique_elements[counts == 1]

        result_list = result.tolist()

        return result_list[0]