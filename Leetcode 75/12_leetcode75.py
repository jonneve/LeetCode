class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # init a sliding window with a left side at index 0, number of flips counter and an answer placeholder
        i = 0
        flips = 0
        ans = 0

        # quick exit check if number of flips allows for length of nums to be flipped, thus answer is len(nums) 
        if k >= len(nums):
            return (len(nums))

        # loop through each number in nums based on its index j (our right side of the sliding window), if nums[j] is 0 increment flips by 1
        # once flips becomes > k, return the length of the sliding window, right - left pointer (this is number of contiguos 1 using all flips possible)
        # then starting at the index of the left side of sliding window, if val is 0 we can decrement flips by one
        # while loop keeps incrementing left side of sliding window by 1 until flips <= k 
        for j in range(len(nums)):
            if nums[j] == 0:
                flips += 1
            if flips > k:
                ans = max(ans, j - i)
            while flips > k:
                if nums[i] == 0:
                    flips -= 1
                i += 1
                
        # max(ans, j - i + 1) proetcts aginst the last x nums all be contiguos 1, 
        # i.e nums = [1,0,1,1], k = 0
        # j will be index of last num (3), i will be index of 1st 1 after flips restored and start of contiguos 1s (2), 3-2 = 1 then + 1 to be inclusve 
        return max(ans, j - i + 1)