class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        # check for attempting to place 0 new flowers as this will allways be true
        if n == 0:
            return True

        # edge case check for start and end of list, check if sum of itself and adjacent value is 0, decrement n if true
        # replaces value if true 
        if flowerbed[0] == 0 and sum(flowerbed[:2]) == 0:
            flowerbed[0] += 1
            n -= 1
        if flowerbed[-1] == 0 and sum(flowerbed[-2:]) == 0:
            flowerbed[-1] += 1
            n -= 1

        # check inner elements, if sum of itself plus adjacent value is 0, decrement n if true
        # replaces value if true 
        for i in range(1, len(flowerbed)-1):
            if sum(flowerbed[i-1:i+2]) == 0:        
                flowerbed[i] += 1
                n -= 1

        # retrun bool if n flowers have been planted
        return n <= 0    