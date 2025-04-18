from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
                
# Create an instance of the Solution class
solution = Solution()

# Call the method directly
nums = [2, 7, 11, 15]  # Example input
target = 9
result = solution.twoSum(nums, target)

# Print the result
print(f"Indexes of numbers that add up to {target}: {result}")