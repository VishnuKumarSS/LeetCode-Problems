class Solution:
    def countOdds(self, low: int, high: int) -> int:
        extra = 0
        if low%2 != 0:
            extra += 1
        if high%2 != 0:
            extra += 1
        
        odd = ((high - low) - extra)//2
        ans = odd + extra
        return ans
