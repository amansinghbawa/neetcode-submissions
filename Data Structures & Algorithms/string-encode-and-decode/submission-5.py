class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}#{s}"
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        index = 0
        res = []
        while(index < len(s)):
            _len = ""
            while s[index] != "#":
                _len += s[index]
                index+=1

            count = int(_len)
            index += 1
            res.append(s[index: index+count])
            index += count
        return res