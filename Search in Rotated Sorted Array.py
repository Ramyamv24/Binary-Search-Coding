class Solution:
    def search(self, nums, target):
        try:
            a = nums.index(target)
            return a
        except ValueError:
            return -1


# Main part
if __name__ == "__main__":
    nums = list(map(int, input("Enter array elements separated by spaces: ").split()))
    target = int(input("Enter target element: "))

    obj = Solution()
    result = obj.search(nums, target)

    print("Index:", result)