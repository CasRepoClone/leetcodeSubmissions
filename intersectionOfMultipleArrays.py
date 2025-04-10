class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """

        # initialise a counting hashmap
        hashmap = {}
        # for every list 
        for l in nums:
            # for every item in the list 
            for item in l:
                # count the items 
                hashmap[item] = hashmap.get(item, 0) + 1
        # create a final resul dict
        final = []
        for key, value in hashmap.items():
            if value == len(nums):
                final.append(key)
            else:pass
        # sort
        final.sort()
        return final

                

        