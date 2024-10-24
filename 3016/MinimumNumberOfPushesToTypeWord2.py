class Solution:
    def minimumPushes(self, word: str) -> int:
        one = {}
        word = list(word) # ["l", "e", "e", "t"]
        for char in word:
            word.append(char)


s = Solution()
print(s.minimumPushes("leet")) # 4