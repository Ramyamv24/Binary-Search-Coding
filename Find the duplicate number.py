from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            ind = abs(nums[i])

            if nums[ind] < 0:
                return ind

            nums[ind] = -nums[ind]

        return -1


# Main function
if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))

    sol = Solution()
    result = sol.findDuplicate(nums)

    print("Duplicate number:", result)