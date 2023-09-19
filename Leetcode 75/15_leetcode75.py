class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # initialise a left and right sum placeholder
        left_sum = 0
        right_sum = 0
    
        # loop through indexes, calc left/right sum using index slicing, excluding current index
        # edge case - when at left/right edge set corresponding side sum to zero
        # retrun pivot index if found else -1
        for i in range(len(nums)):
            if i == 0:
                left_sum = 0
            else:
                left_sum = sum(nums[:i])

            if i == len(nums) - 1:
                right_sum = 0
            else:
                right_sum = sum(nums[i+1:])

            if left_sum == right_sum:
                return i
        return -1