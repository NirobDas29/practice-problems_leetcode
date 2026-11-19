class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        st =[]
        ans = [-1]*n
        for i in range(2*n,-1,-1):
            num = nums [i % n ]
            while st and st[-1] <= num:
                st.pop()
            if i < n and st:
                ans[i] = st[-1]
            st.append(num)
        return ans

        