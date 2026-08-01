class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        l   = []
        ch  = "" 
        for num in nums :
            if ch.find(","+str(num)+",") == -1:
                l.append({"num" :num ,"nbOc" : nums.count(num)})
            ch += ","+str(num)+","
        l.sort(key = lambda item : item["nbOc"] ,reverse = True)
        print(l)
        for i in range(k):
            res.append(l[i]["num"])
        return res


