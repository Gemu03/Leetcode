from typing import List

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        revealed = []
        while deck:
            if revealed:
                revealed.insert(0, revealed.pop())
            revealed.insert(0, deck.pop())
        return revealed
    
s = Solution()
print(s.deckRevealedIncreasing([17,13,11,2,3,5,7])) # [2,13,3,11,5,17,7]


