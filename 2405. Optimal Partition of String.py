class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
         # using the hashmap like a cache 
        # aim is to use a counting hash map
        freqMap = {}
        splitPos = []
        cache = []
        tempString = ""

        for char in s:
            # check if the char is in the hashmap and increment by 1, if not add it to hashmap
            freqMap[char] = freqMap.get(char, 0) + 1 
            # increment counter to count position in string 

            # if the character occurs more than once 
            if freqMap.get(char, 0) > 1:
                # add the split string 
                cache.append(tempString)
                # reset the string and add the starting char 
                tempString = char
                # and reset the hashmap with the new char as 1
                freqMap = {}; freqMap[char] = freqMap.get(char, 0) + 1 
            else:
                # build our temp string 
                tempString += char
            
        
            
        if tempString != "":
            cache.append(tempString)
        return int(len(cache))
            