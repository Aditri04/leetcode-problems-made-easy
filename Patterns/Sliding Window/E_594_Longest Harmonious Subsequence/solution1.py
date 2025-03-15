class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counthashmap = {}
        for i in range(len(nums)):
            if nums[i] not in counthashmap:
                counthashmap[nums[i]] = 1
                continue
            counthashmap[nums[i]]+=1
        LHSsize = 0
        for key, value in counthashmap.items():
            if key+1 in counthashmap:
                LHSsize = max(value+counthashmap[key+1], LHSsize)
        return LHSsize