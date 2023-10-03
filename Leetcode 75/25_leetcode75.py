class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """

        # instantiate a list of the string and a placeholder for answer
        list_s = list(s)
        ans = []

        # for loop looking for * char in s, if found appned the char to ans placeholder, else pop the last element from char off the list and skip the * element
        # retrun the joined up string representation of ans once done
        for char in list_s:
            if char != "*":
                ans.append(char)
            else:
                ans.pop()
    
        return ''.join(ans)