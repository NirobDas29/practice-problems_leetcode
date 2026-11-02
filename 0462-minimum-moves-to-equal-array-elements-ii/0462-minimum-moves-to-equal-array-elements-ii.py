class Solution:
    def minMoves2(self, nums):
        nums.sort()
        median = nums[len(nums)//2]
        moves =0
        for n in nums:
            moves +=abs(n-median)
        return moves
        