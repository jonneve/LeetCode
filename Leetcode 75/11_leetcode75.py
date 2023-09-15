class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        # instantiate a var for the lowercase vowels, an answer and a temporary count placeholder
        vowels = 'aeiou'
        count = 0
        ans = 0

        # loop through each char in s based on index, if present in vowels then increment count by 1 
        # once index is >= k - 1 (reached kth char in s with 0 based index), calc the max of ans and count, this creates a sliding window of k elements of s
        # if the char leaving the window was a vowel then decrement count by 1, then the next for loop will incrment if incoming char to window is a vowel 
        for i in range(len(s)):
            if s[i] in vowels:
                count += 1
            if i >= k - 1:
                ans = max(ans, count)
                if s[i + 1 - k] in vowels: 
                    count -= 1

        return ans 