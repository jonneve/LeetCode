class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        # empty list to hold alternate index-based chars of each word upto the length of the shortest string
        answer = []

        for i in range(len(min(word1,word2, key=len))):
            answer.append(word1[i])
            answer.append(word2[i])


        # if words are unequal length append the additonal chars onto the end of teh list
        if len(word1) != len(word2):
            answer.append(max(word1,word2, key=len)[len(min(word1,word2, key=len)):])
            
        # return the list back as a meregd string    
        return(''.join(answer))

