class Solution:
    def minRemoveToMakeValid(self, s):
        stack = []
        remove = set()
        for i, char in enumerate(s):
            if char == '(':stack.append(i)
            elif char == ')':
                if stack:stack.pop()
                else:remove.add(i)
        remove = remove.union(set(stack))
        return ''.join([char for i, char in enumerate(s) if i not in remove])

s = Solution()
print(s.minRemoveToMakeValid("lee(t(c)o)de)"))
print(s.minRemoveToMakeValid("a)b(c)d"))
print(s.minRemoveToMakeValid("))(("))