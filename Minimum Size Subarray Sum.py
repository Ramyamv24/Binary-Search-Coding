class Solution:
    def minSubArrayLen(self, target, nums):
        left, summ, m = 0, 0, float('inf')

        for i in range(len(nums)):
            summ += nums[i]

            while summ >= target:
                m = min(m, i - left + 1)
                summ -= nums[left]
                left += 1

        return 0 if m == float('inf') else m


# Main part
if __name__ == "__main__":
    target = int(input("Enter target sum: "))
    nums = list(map(int, input("Enter array elements separated by spaces: ").split()))

    obj = Solution()
    result = obj.minSubArrayLen(target, nums)

    print("Minimum subarray length:", result)