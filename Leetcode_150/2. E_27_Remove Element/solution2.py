class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        forward_cnt = 0
        backward_cnt = len(nums) -1
        if backward_cnt == -1:
            return 0
        while nums[backward_cnt]==val and backward_cnt>-1:
            backward_cnt-=1
        while forward_cnt<=backward_cnt:
            if nums[forward_cnt] == val:
                nums[forward_cnt] = nums[backward_cnt]
                forward_cnt+=1
                backward_cnt-=1
                while nums[backward_cnt]==val:
                    backward_cnt-=1
            else:
                forward_cnt+=1
        return forward_cnt
            