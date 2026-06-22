"""
LeetCode 485 — Max Consecutive Ones
https://leetcode.com/problems/max-consecutive-ones/
Difficulty: Easy

Given a binary array nums, return the maximum number of consecutive 1's
in the array.

Example 1:
    Input:  nums = [1,1,0,1,1,1]
    Output: 3
    Explanation: The first two digits or the last three digits are
    consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:
    Input:  nums = [1,0,1,1,0,1]
    Output: 2

Constraints:
    1 <= nums.length <= 10^5
    nums[i] is either 0 or 1.
"""
from typing import List


def find_max_consecutive_ones(nums: List[int]) -> int:
    cnc = 0
    res = 0
    for n in nums:
        if n == 1:
            cnc += 1
            res = max(res, cnc)
        else:
            cnc = 0
    return res


if __name__ == "__main__":
    # (nums, expected)
    cases = [
        ([1, 1, 0, 1, 1, 1], 3),
        ([1, 0, 1, 1, 0, 1], 2),
        ([0], 0),
        ([1], 1),
        ([1, 1, 1, 1], 4),
    ]
    for nums, expected in cases:
        result = find_max_consecutive_ones(nums)
        assert result == expected, (
            f"find_max_consecutive_ones({nums}) -> {result}, expected {expected}"
        )
    print("All tests passed.")
