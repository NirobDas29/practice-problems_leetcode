class Solution:
    def shipWithinDays(self, weights, days):
        low = max(weights)
        high = sum(weights)

        ans = high

        while low <= high:
            mid = (low + high) // 2

            if self.canShip(weights, days, mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

    def canShip(self, weights, days, cap):
        d = 1
        cu = 0

        for w in weights:
            if cu + w > cap:
                d += 1
                cu = w
            else:
                cu += w

        return d <= days