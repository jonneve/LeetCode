class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # find the count of 0s in the list, remove the first occuring 0 and append it to end of list for n instances
        for i in range(nums.count(0)):
            nums.remove(0)
            nums.append(0)

        return nums