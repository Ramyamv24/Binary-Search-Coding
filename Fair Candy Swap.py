class Solution(object):
    def fairCandySwap(self, Alice, Bob):
        dif = (sum(Alice) - sum(Bob)) // 2
        A = set(Alice)

        for i in set(Bob):
            if dif + i in A:
                return [dif + i, i]


def main():
    alice = list(map(int, input("Enter Alice's candies: ").split()))
    bob = list(map(int, input("Enter Bob's candies: ").split()))

    sol = Solution()
    result = sol.fairCandySwap(alice, bob)

    print("Swap:", result)


if __name__ == "__main__":
    main()