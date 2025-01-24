from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start, path):
            result.append(path[:])
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return result
    
solution = Solution()
input_nums = list(map(int, input().split()))
output = solution.subsets(input_nums)  # Call subsets function with the input
print(output)  