class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        # pointers for start/end of int list (j - 1 for 0 based index), ans as placeholder for instances where i + j = k
        i = 0
        j = len(nums) - 1
        ans = 0

        # sort list so pointer can be incremented in correct direction based on if i + j > or < k
        nums.sort()

        # while loop will terminate when i >= j, so as we directionally increment/decrement i/j based on the value of k, once max number of instances where i + j = k
        # is found the while loop will terminate. ans, i, j get incremenetd/decremented accordingly when i + j = k (ans goes up, left pointer >, right pointer <)
        while i < j:
            if (nums[i] + nums[j]) == k:
                ans += 1
                i += 1
                j -= 1 
            elif nums[i] + nums[j] > k:
                j -= 1
            else:
                i += 1

        return ans