class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        # gcd helper function that recursively calls function until the b param is 0 (where b is the modulo)
        # if modulo of a % b != 0 then value of b will be the modulo, a the previous denomiator, and the function is recalled
        def get_gcd(a, b):
            if(b == 0):
                return a
            else:
                return get_gcd(b, a % b)

        # if both strings are not equal when concatted in both combinations then they are not a gcd of strings
        if str1 + str2 != str2 + str1:
            return ""
        # else return the string pattern that is the slice of string1 upto the gcd index of the string
        else:
            return str1[:get_gcd(len(str1), len(str2))]