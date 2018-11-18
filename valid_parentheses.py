#! /usr/bin/python

# https://leetcode.com/problems/valid-parentheses/description/
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.


class Solution(object):
    
    def isValid(self, s):
        OPENING_BRACKETS = {"{", "[", "("}
        BRACKETS_MAP = {"]": "[", "}": "{", ")": "("}
        stack = []
        for bracket in s:
            if bracket in OPENING_BRACKETS:
                stack.append(bracket)
            elif not stack:
                print "false"
                return False       
            elif stack.pop() != BRACKETS_MAP[bracket]:
                print "false"
                return False       
        print "true"
        return not stack


solution = Solution()
solution.isValid("()")


