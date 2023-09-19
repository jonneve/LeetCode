class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # initialise vars and answer placeholder
        i = 0
        j = 0
        ans = 0

        # quick check to see if nums is all 1s, if so we must delete 1 element and return val as max len of subarray
        if sum(nums) == len(nums):
            return len(nums) - 1

        # loop through each element, incrment the counter j when element is 1
        # when element is 0, ans is the max of counter j + i (where i was previous max contiguos coun, but init val is 0) iteratively
        # then set i to be j, so now i will function as the previous max contiguos count, then refind j. 
        # i.e ans = max (previous max, previous contigous count + current contigous count) this give max subarray length of two contigous arrays of 1s with only a single 0 between them
        for num in nums:
            if num == 1:
                j += 1
            else:
                ans = max(ans, i + j)
                i = j
                j = 0  
        ans = max(ans, i + j)

        return ans