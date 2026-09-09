import math
class Solution:
    def find_ceil(self, piles, mid):
        total_hours=0
        for pile in piles:
            total_hours+=math.ceil(pile/mid)
        return total_hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start=1
        end=max(piles)
        ans=float("INF")
        while(start<=end):
            mid=(start+end)//2
            total_hours=self.find_ceil(piles, mid)
            if total_hours<=h:
                ans=mid
                end=mid-1
            else:
                start=mid+1
        return ans
        