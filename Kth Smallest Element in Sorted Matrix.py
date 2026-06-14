from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        L = []
        for i in matrix:
            for j in i:
                L.append(j)
        L.sort()
        return L[k - 1]

# Main part
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []
print("Enter the matrix row by row:")

for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

k = int(input("Enter k: "))

obj = Solution()
print("Kth smallest element:", obj.kthSmallest(matrix, k))