class Solution(object):
    def findPeakElement(self, nums):
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1

        return l


# Main part
nums = list(map(int, input("Enter array elements separated by spaces: ").split()))

sol = Solution()
peak_index = sol.findPeakElement(nums)

print("Peak element index:", peak_index)
print("Peak element:", nums[peak_index])