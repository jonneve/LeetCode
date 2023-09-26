class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        # make a list from the string split by spaces, with leading/trailing spaces removed
        s_list = s.strip().split(' ')

        # remove any instances of multiple spaces between a word, i.e. if list contains empty space after split
        while '' in s_list:
            s_list.remove('')

        # placeholder var for the anser 
        ans = []

        # loop through the cleaned string in reverse order, appending it to answer list then retrun that list joined with a space between elements
        for i in range(len(s_list)-1,-1,-1):
            ans.append(s_list[i])

        return ' '.join(ans)