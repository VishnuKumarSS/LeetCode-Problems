from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashes = {}
        
        for ind,num in enumerate(nums):
            other_num = target - num 

            if other_num in hashes:
                return [hashes[other_num],ind]

            hashes[num] = ind     
        