class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # place holder for i, j pointer (j - 1 for 0 based index) and a temp for answer which is max area
        ans = 0 
        i = 0
        j = len(height) - 1

        # while there is a diff between the two pointers, find diff between x co ords to be our width
        # height is min of the two y vals to simulate the water container, update answer if area > temp answer
        # move pointrers based on which y val is higher as this will find the max area
        # while loop terminates arfter pointers are equal then the temp max height is greatest area found in solution
        while i < j:
            width = j - i
            area = width * min(height[i], height[j])
            ans = max(area, ans)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return ans 