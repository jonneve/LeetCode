# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        # instantiate left and right var for mid point searching
        left = 0
        right = n

        # if the initial response from guess n isnt the right number, continually find the midpoint between left and right using int division
        # now, until the response from guess() with this midpoint is the right number, keep looping through
        # if response is smaller than pick, increment left to the midpoint then re-find mid
        # if response is larger than pick, decrement right to the midpoint then re-find mid
        while guess(n) != 0:
            mid = (left + right) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == 1:
                left = mid + 1
            else:
                right = mid - 1
        return n