"""
LeetCode 1929 — Concatenation of Array
https://leetcode.com/problems/concatenation-of-array/
Difficulty: Easy

Given an integer array nums of length n, you want to create an array ans of
length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for
0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.

Example 1:
    Input:  nums = [1,2,1]
    Output: [1,2,1,1,2,1]
    Explanation: The array ans is formed as follows:
    - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
    - ans = [1,2,1,1,2,1]

Example 2:
    Input:  nums = [1,3,2,1]
    Output: [1,3,2,1,1,3,2,1]
    Explanation: The array ans is formed as follows:
    - ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
    - ans = [1,3,2,1,1,3,2,1]

Constraints:
    n == nums.length
    1 <= n <= 1000
    1 <= nums[i] <= 1000
"""
from typing import List


def get_concatenation(nums: List[int]) -> List[int]:
    ans = []
    n = 2
    for i in range(n):
        for j in nums:
            ans.append(j)
    return ans


if __name__ == "__main__":
    # (nums, expected)
    cases = [
        ([1, 2, 1], [1, 2, 1, 1, 2, 1]),
        ([1, 3, 2, 1], [1, 3, 2, 1, 1, 3, 2, 1]),
        ([5], [5, 5]),
    ]
    for nums, expected in cases:
        result = get_concatenation(nums)
        assert result == expected, (
            f"get_concatenation({nums}) -> {result}, expected {expected}"
        )
    print("All tests passed.")
