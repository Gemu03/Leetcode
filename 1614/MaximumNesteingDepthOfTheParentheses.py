class Solution:
    def maxDepth(self, s: str) -> int:
        ans = [*s]
        fin = []
        count = 0
        max = 0
        for val in ans:
            if val == "(" or val == ")": fin.append(val)
        for val in fin:
            if val == '(':  count += 1
            if val == ')':  count -= 1
            if count > max:  max = count
        return max
