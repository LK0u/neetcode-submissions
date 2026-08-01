class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = []
        while len(strs) >0:
            t = [strs[0]]
            j = 1
            while j <= len(strs) -1:
                if isAnagram(strs[0] ,strs[j]):
                    t.append(strs[j])
                    strs.pop(j)
                    j -= 1
                j += 1
            strs.pop(0)
            l.append(t)
        return l


def isAnagram(s ,t):
    ok = len(s) == len(t)
    i = -1
    while ok and i <= len(s)-2:
        i += 1
        idx = t.find(s[i])
        ok = ok and idx != -1
        t = t[:idx] + t[idx+1:]
    return ok


