from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        lista = []
        def is_palindrome(s):
            return s == s[-1]
        
        def reverso(start, path):
            if start == len(s):
                lista.append(path)
                return
            for i in range(start, len(s)):
                if is_palindrome(s[start:i+1]):
                    reverso(i+1, path + [s[start:i+1]])
        reverso(0, [])
        
        return lista
    
s = Solution()
print(s.partition("aab")) # [["a","a","b"],["aa","b"]]
print(s.partition("a")) # [["a"]]