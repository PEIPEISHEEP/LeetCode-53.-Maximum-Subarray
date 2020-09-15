class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = g = -sys.maxsize
        for n in nums:
            l = max(n,l+n)
            print("l:",l," g:",g)
            g = max(l,g)
            
        return g