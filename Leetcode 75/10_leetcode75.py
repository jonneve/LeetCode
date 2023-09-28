class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        # shortcut if k is the length of the list
        if k == len(nums):
            return sum(nums) / float(k)

        # find the starting moving sum from nums[0<->k], then this is our current max and placeholder moving sum
        _max = sum(nums[:k])
        _sum = _max

        # loop through from k till the end of the list, subtracting the first element of our previous moving sum and adding the next element. this creates a moving sum.
        # replace the max if the new moving sum is greater than the previous max. Return max / k cast as a float to give precision to the avg
        for i in range(k, len(nums)):
            _sum -= nums[i - k]
            _sum += nums[i]
            _max = max(_sum, _max)

        return _max / float(k)