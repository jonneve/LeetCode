class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        # check for n values less than 3 as tri[] statement requires a slice of i-3 : i to calc tri[n]
        if n == 0 or n == 1:
            return n
        elif n == 2:
            return 1

        # if n >= 3, create a placeholder tri list with all elemnts initialised to 1 and replace 1st element with 0 to create initial correct sequence[0,1,1...] 
        # then using a sliding window-like slice of the sum of the previous 3 elements, iteratively calc the current val of tri[n] then continue
        else:
            tri = [1] * (n + 1)
            tri[0] = 0
            for i in range(3, n + 1):
                tri[i] = sum(tri[i - 3:i])
            return tri[n]    