class Solution:
    def triangleNumber(self, nums):
        n = len(nums)
        totaltri = 0
        nums.sort()

        for longest in range(n - 1, 1, -1):
            l, m = 0, longest - 1

            while l < m:
                if nums[l] + nums[m] > nums[longest]:
                    totaltri += m - l
                    m -= 1
                else:
                    l += 1

        return totaltri


# Main part
nums = list(map(int, input("Enter the side lengths separated by spaces: ").split()))

sol = Solution()
result = sol.triangleNumber(nums)

print("Number of possible triangles:", result)