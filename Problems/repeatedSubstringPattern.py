class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # concat the two strings together, then remove the trailing charecters
        string_concat = (s + s)[1:-1]
        
        # now if original s is present in the concat wihtout leading/trailing char then s is the repition of a substring of s
        # ie eg1 - string_concat = a"bababa"b where 'abab' is in the concat without the leading/trailing chars
        # wihtout the leading/trailing chars a substring of 'abab' must be present and repeated i.e 'ab'
        return s in string_concat