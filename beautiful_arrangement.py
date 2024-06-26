'''Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement if for every i (1 <= i <= n), either of the following is true:

perm[i] is divisible by i.
i is divisible by perm[i].
Given an integer n, return the number of the beautiful arrangements that you can construct.



Example 1:

Input: n = 2
Output: 2
Explanation:
The first beautiful arrangement is [1,2]:
    - perm[1] = 1 is divisible by i = 1
    - perm[2] = 2 is divisible by i = 2
The second beautiful arrangement is [2,1]:
    - perm[1] = 2 is divisible by i = 1
    - i = 2 is divisible by perm[2] = 1
    https://leetcode.com/problems/beautiful-arrangement/description/'''
class BeautifulArrangement:
    def countArrangement(self, n: int) -> int:
        self.res = 0
        nums = [i for i in range(1, n+1)]

        def dfs(nums: list, i: int = 1):
            if i == n+1:
                self.res += 1
                return

            for j, num in enumerate(nums):
                if not(num % i and i % num):
                    dfs(nums[:j] + nums[j+1:], i+1)

        dfs(nums)
        return self.res