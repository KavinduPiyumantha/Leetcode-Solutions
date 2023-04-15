from typing import List
from Solution import Solution

def main():
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    result = solution.twoSum(nums, target)
    print(result)

if __name__ == "__main__":
    main()