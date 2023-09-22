class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # init a placeholder for the count of matches
        count = 0

        # loop through the index for the count of rows, then create a transposed column lsit using that index position from eahc row
        # then count the occurances each column is found in the original grid rows  
        for i in range(len(grid)):
            column = []
            for row in grid:
                column.append(row[i])
            count += grid.count(column) 

        return count