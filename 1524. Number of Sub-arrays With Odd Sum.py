from typing import List
arr = [1,3,5]

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        ans = 0
        for i in range(len(arr)):
            sub_num = 0
            for j in range(i, len(arr)):
                sub_num += arr[j]
                if sub_num%2 != 0:
                    ans += 1
        return ans

solution = Solution()
print(solution.numOfSubarrays(arr))

from typing import List
arr = [1,3,5]

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        ans = 0
        for i in range(len(arr)):
            sub_num = 0
            for j in range(i, len(arr)):
                sub_num += arr[j]
                if sub_num%2 != 0:
                    ans += 1
        return ans

solution = Solution()
print(solution.numOfSubarrays(arr))