import numpy as np
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        arr1 = np.array(nums1)
        arr2 =np.array(nums2)
        combining = np.concatenate((arr1, arr2))
        combining.sort()
        
        n = len(combining)
        #checking if its odd
        if n%2 ==1:
            return  float(combining[n // 2])
        else:
            return  (combining[(n // 2) - 1] + combining[n // 2]) / 2.0

            
        