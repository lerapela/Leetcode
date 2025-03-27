class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_map  = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        Total =0
        pre_value =0

        for char in reversed(s):
            current_value = roman_map[char]
            if current_value < pre_value:
                Total -= current_value
            else:
                Total += current_value
            pre_value = current_value 
        return Total
        