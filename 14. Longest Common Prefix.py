from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        check = ""
        ans = ""
        index = 0
        end = False
        while end==False:
            ans += check
            first = True
            for word in strs:
                if index >= len(word):
                    end = True
                    break
                if len(word) == 0:
                    ans = word
                    end = True
                    break
                if first:
                    first = False
                    check = word[index]
                elif word[index] != check:
                    end = True
                    break

            index += 1
        return ans

solution = Solution().longestCommonPrefix

print(solution(["flower","flow","flight"]))
print(solution(["dog","racecar","car"]))

print(solution(["a"]))
print(solution(["flower","flower","flower","flower"]))