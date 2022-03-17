class Solution(object):
  def scoreOfParentheses(self, s):
    stack = [];
    cur = 0;
    for c in s:
      if c == '(':
        stack.append(cur);
        cur = 0;
      else:
        cur = stack.pop() + max(1, cur*2);
    return cur;

#https://leetcode.com/problems/score-of-parentheses/