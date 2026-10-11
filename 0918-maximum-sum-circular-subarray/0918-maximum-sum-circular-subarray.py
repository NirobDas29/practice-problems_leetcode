class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        globalmax = nums[0]
        globalmin = nums[0]
        currmax = 0
        currmin = 0
        total = 0
        for n in nums:
            currmax = max(currmax+n,n)
            currmin = min(currmin+n,n)
            total += n
            globalmax = max(currmax,globalmax)
            globalmin = min(currmin,globalmin)
    
        return max(globalmax,total - globalmin) if globalmax > 0 else globalmax
        
        