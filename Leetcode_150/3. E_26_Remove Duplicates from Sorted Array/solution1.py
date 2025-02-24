class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniquecnt = 0
        for ind in range(1, len(nums)):
            if not nums[ind] == nums[uniquecnt]:
                uniquecnt +=1
                nums[uniquecnt] = nums[ind]
        return uniquecnt+1