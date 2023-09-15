class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        # turn s to a list so it can be looped through by index, make vowel list with possible case handling
        s = list(s)
        vowels = list('aieou' + 'aieou'.upper())
        # i,j will be index pointers to tarverse through the lists
        i, j = 0, len(s) - 1
        
        # until i and j meet in the list, i will incrementally look through elemenst untill a vowel is found, j will do the same from the end
        # if both i and j have found a vowel char, then the values are swapped then, then pointers continue
        # no 1 of fewer voewels are found the increment/decrmenet will continue and i will = j eventually with no swaps
        while i < j:
            if s[i] not in vowels:
                i += 1
                continue
                
            if s[j] not in vowels:
                j -= 1
                continue
                
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
            
        return ''.join(s)