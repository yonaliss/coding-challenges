"""
LeetCode 1299 — Replace Elements with Greatest Element on Right Side
https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
Difficulty: Easy

Given an array arr, replace every element in that array with the greatest
element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

Example 1:
    Input:  arr = [17,18,5,4,6,1]
    Output: [18,6,6,6,1,-1]
    Explanation:
    - index 0 --> the greatest element to the right of index 0 is 18.
    - index 1 --> the greatest element to the right of index 1 is 6.
    - index 2 --> the greatest element to the right of index 2 is 6.
    - index 3 --> the greatest element to the right of index 3 is 6.
    - index 4 --> the greatest element to the right of index 4 is 1.
    - index 5 --> there are no elements to the right of index 5, so we put -1.

Example 2:
    Input:  arr = [400]
    Output: [-1]
    Explanation: There are no elements to the right of index 0.

Constraints:
    1 <= arr.length <= 10^4
    1 <= arr[i] <= 10^5
"""
from typing import List


def replace_elements(arr: List[int]) -> List[int]:
    maxvalue = -1
    for i in range(len(arr) - 1, -1, -1):
        newmaxvalue = max(arr[i], maxvalue)
        arr[i] = maxvalue
        maxvalue = newmaxvalue
    return arr

if __name__ == "__main__":
    # (arr, expected)
    cases = [
        ([17, 18, 5, 4, 6, 1], [18, 6, 6, 6, 1, -1]),
        ([400], [-1]),
        ([1, 2], [2, -1]),
        ([5, 5, 5], [5, 5, -1]),
    ]
    for arr, expected in cases:
        original = list(arr)
        result = replace_elements(arr)
        assert result == expected, (
            f"replace_elements({original}) -> {result}, expected {expected}"
        )
    print("All tests passed.")
