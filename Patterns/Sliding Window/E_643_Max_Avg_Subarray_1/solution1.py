class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sumofk = 0
        maxavg = -99999
        for i in range(len(nums)):
            sumofk+=nums[i]
            if i>=k-1:
                maxavg = max(maxavg, sumofk/k)
                sumofk-=nums[i-k+1]   
        return maxavg