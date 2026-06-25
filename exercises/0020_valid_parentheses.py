"""
LeetCode 20 — Valid Parentheses
https://leetcode.com/problems/valid-parentheses/
Difficulty: Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and
']', determine if the input string is valid.

An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
    Input:  s = "()"
    Output: true

Example 2:
    Input:  s = "()[]{}"
    Output: true

Example 3:
    Input:  s = "(]"
    Output: false

Example 4:
    Input:  s = "([])"
    Output: true

Constraints:
    1 <= s.length <= 10^4
    s consists of parentheses only '()[]{}'.
"""


def is_valid(s: str) -> bool:
    parentheses = {')': '(', '}': '{', ']': '['}
    stack = []
    for p in s:
        if p in parentheses:
            if not stack or stack.pop() != parentheses[p]:
                return False
        else:
            stack.append(p)
    return not stack



if __name__ == "__main__":
    # (s, expected)
    cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([])", True),
        ("([)]", False),
        ("]", False),
    ]
    for s, expected in cases:
        result = is_valid(s)
        status = "OK " if result == expected else "FAIL"
        print(f"[{status}] is_valid({s!r}) -> {result}, expected {expected}")
