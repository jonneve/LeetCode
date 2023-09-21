class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        
        # instantiae placeholder for arrays diff list elements
        ans1 = []
        ans2 = []

        # loop through each number in a set of the two lists
        # if not in num1/num2 (thus in num2/num1 due to it being a set) append to placeholder list
        # return list of lists as per the expected return type
        for num in set(nums1+nums2):
            if num not in nums2:
                ans1.append(num)
            elif num not in nums1:
                ans2.append(num)
        return [ans1, ans2]