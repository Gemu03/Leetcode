from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in set(deadends):  return -1
        if '0000' == target:  return 0
        
        deadends = set(deadends)
        visited = set()
        visited.add('0000')
        queue = ['0000']
        steps = 0
        while queue:
            steps += 1
            for _ in range(len(queue)):
                current = queue.pop(0)
                for i in range(4):
                    for j in [1, -1]:
                        new = current[:i] + str((int(current[i]) + j) % 10) + current[i+1:]
                        if new == target:
                            return steps
                        if new not in deadends and new not in visited:
                            visited.add(new)
                            queue.append(new)
        return -1








s = Solution()
print(s.openLock(["0201","0101","0102","1212","2002"], "0202")) # 6
print(s.openLock(["8888"], "0009")) # 1
print(s.openLock(["8887","8889","8878","8898","8788","8988","7888","9888"], "8888")) # -1


print(s.openLock(["5557","5553","5575","5535","5755","5355","7555","3555","6655","6455","4655","4455","5665","5445","5645","5465","5566","5544","5564","5546","6565","4545","6545","4565","5656","5454","5654","5456","6556","4554","4556","6554"], "5555")) # -1