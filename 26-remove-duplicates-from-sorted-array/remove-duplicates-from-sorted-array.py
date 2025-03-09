import numpy as np
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        store =[]
        arr1 =np.array(nums)
       
        unique_arr = np.unique(arr1)
        
        
        nums[:] = unique_arr.tolist()
        
        
        return len(unique_arr)

        