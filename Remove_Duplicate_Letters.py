class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        rindex = {c: i for i,c in enumerate(s)}
        result = []
        for i, c in enumerate(s):
            if c not in result:
                while (result and c < result[-1] and i < rindex[result[-1]]):
                    result.pop()
                result.append(c)
        return ''.join(result)        