class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start = 0
        end = len(nums) -1
        while start<=end:
            if nums[end] == val:
                end-=1
                continue
            if not nums[start] == val:
                start +=1
            else:
                nums[start] = nums[end]
                end -=1
                start+=1
        return end+1