from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            for j in range((i+1),len(nums)):
                if((nums[i]+ nums[j]) == target):   
                    result.append(i)
                    result.append(j)
                    return result
        return result


# nums = [2, 7, 11, 15]
# target = 9
# solution = Solution()
# result = solution.twoSum(nums, target)
# print(result)