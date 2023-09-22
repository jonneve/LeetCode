class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """

        # placeholder lists for a word map of each string
        w1_map = []
        w2_map = []

        # exit check, if lists are uneven lengths then no amount of operations will result in matching strings 
        # similarly if the set representation of each string is different then they dont have matching chars required to be close
        if (len(word1) != len(word2)) or (set(word1) != set(word2)):
            return False

        # now create a word map of the count of each unique char in each string using set()
        # if these two word maps are equal once sorted the occurances of each unique char are the same just the chars might not be the same
        # but with unlimited number of opertation 1s they can be as by swapping 2 simultaneously will not effect the result of the sorted word map
        for char in set(word1):
            w1_map.append(word1.count(char))
        for char in set(word2):
            w2_map.append(word2.count(char))

        w1_map.sort()
        w2_map.sort()

        return w1_map == w2_map