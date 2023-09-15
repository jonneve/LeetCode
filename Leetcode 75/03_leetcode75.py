class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """      

        # init placeholder for answers, cached var of max
        answer = []
        _max = max(candies)

        # iterate through candies list, if value + extra candies is greater than or equal to existing max candies append a true to answer list
        for i in candies:
            # use a var for max so expensive function is not repeatedly called
            if i + extraCandies >= _max:
                answer.append(True)
            else:
                answer.append(False)

        return answer