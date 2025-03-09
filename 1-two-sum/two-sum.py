class Solution(object):
    def twoSum(self, nums, target):

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        occur = {}  
        for i,num in enumerate(nums):

            results = target - num
            if results in occur:
                return [occur[results],i]
                 
            occur[num] = i
        return [] 
