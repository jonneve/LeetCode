class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # loop through s string, use find method which returns 0 based index if found, else -1
        # adding 1 will mean i = 0 if cahr not in t, else we slice t the remove chars up to and including the index of the find method
        for char in s:
            i = t.find(char) + 1
            if i == 0:
                return False
            else:
                t = t[i:]
        return True