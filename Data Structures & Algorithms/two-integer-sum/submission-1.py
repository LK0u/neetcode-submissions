class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ok = False 
        p = -1
        while not ok and p <= len(nums) -3:
            p += 1
            i = p +1
            while not ok and i <= len(nums) -1:
                ok = (nums[p] + nums[i]) ==  target
                i += 1
            
        return [p ,i-1]
