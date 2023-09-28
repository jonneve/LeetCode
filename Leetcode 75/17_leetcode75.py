class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        # placeholder to hold count of each distinct element
        ans = []

        # loop through the array as a set, then append the count of the occurances of each element in the initial array to a list
        # the len of both the array and the ans lists should be equal if the number of occurrences of each value in the array is unique
        for num in set(arr):
            ans.append(arr.count(num))

        return len(set(arr)) == len(set(ans))