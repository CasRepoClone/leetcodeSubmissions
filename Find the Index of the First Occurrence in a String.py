class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # we're going to use a sliding window for this to spot it
        
        # obviously left pointer being set to 0 
        left = 0
        # and for the length of the word to the right pointer
        right = len(needle) 

        # between the length of the word to the end 
        for i in range(len(needle), len(haystack)):
            # if the window matches the word 
            if str(haystack[left:right]) == needle:
                # return first occurance 
                return left
            # increment the sliding window 
            left, right = left + 1, right + 1
        # if nothing is found return -1 
        return -1

        