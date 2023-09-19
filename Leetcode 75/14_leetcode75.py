class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        
        # intiliase altitude vars
        current_alt = 0
        max_alt = 0

        # loop through each element, calculate the altitude of each point then iteratively set the max and return it after the loop
        for i in gain:
            current_alt += i
            max_alt = max(max_alt, current_alt)

        return max_alt