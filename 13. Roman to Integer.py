s = "MCMXCIV"
values = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
}
class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        passs = 0
        for letter in range(len(s)):
            if passs != 0:
                passs = 0
                continue
            if letter != len(s)-1:
                if values[s[letter]] < values[s[letter+1]]:
                    ans += abs(values[s[letter+1]] - values[s[letter]])
                    passs += 1
                elif values[s[letter]] > values[s[letter+1]] or values[s[letter]] == values[s[letter+1]]:
                    ans += values[s[letter]]
            else:
                ans += values[s[letter]]
        return ans +1

solution = Solution().romanToInt
print(solution(s))