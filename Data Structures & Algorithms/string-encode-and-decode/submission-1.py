class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for Str in strs:
            for c in Str:
                res += chr((ord(c)+1) %256)
            res += "😀"
        return res

    def decode(self, s: str) -> List[str]:
        t = ""
        l = []
        i = -1
        while i <len(s)-1:
            i += 1
            if not s[i] == "😀":
                t += chr((ord(s[i])-1) %256)
            else :
                l.append(t)
                t = ""
        return l
