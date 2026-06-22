"""
LeetCode 27 — Remove Element
https://leetcode.com/problems/remove-element/
Difficulty: Easy

Given an integer array nums and an integer val, remove all occurrences of val
in nums in-place. The order of the elements may be changed. Then return the
number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k. To get
accepted, you need to do the following things:

- Change the array nums such that the first k elements of nums contain the
  elements which are not equal to val. The remaining elements of nums are not
  important, as well as the size of nums.
- Return k.

Example 1:
    Input:  nums = [3,2,2,3], val = 3
    Output: 2, nums = [2,2,_,_]
    Explanation: Your function should return k = 2, with the first two elements
    of nums being 2. The order of the elements may change.

Example 2:
    Input:  nums = [0,1,2,2,3,0,4,2], val = 2
    Output: 5, nums = [0,1,4,0,3,_,_,_]

Constraints:
    0 <= nums.length <= 100
    0 <= nums[i] <= 50
    0 <= val <= 100
"""
from typing import List


def remove_element(nums: List[int], val: int) -> int:
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k], nums[i] = nums[i], nums[k]
            k += 1
    return k



if __name__ == "__main__":
    # (nums, val, expected_k, expected_kept) — order of the first k elements
    # doesn't matter, so we compare them as multisets.
    cases = [
        ([3,2,2,3], 3, 2, [2, 2]),
        ([0,1,2,2,3,0,4,2], 2, 5, [0, 1, 4, 0, 3]),
        ([], 0, 0, []),
        ([1, 1, 1], 1, 0, []),
        ([4, 5], 6, 2, [4, 5]),
    ]
    for nums, val, expected_k, expected_kept in cases:
        original = list(nums)
        k = remove_element(nums, val)
        assert k == expected_k, (
            f"remove_element({original}, {val}) -> {k}, expected {expected_k}"
        )
        assert sorted(nums[:k]) == sorted(expected_kept), (
            f"remove_element({original}, {val}) left nums[:{k}] = {nums[:k]}, "
            f"expected the multiset {expected_kept}"
        )
    print("All tests passed.")
