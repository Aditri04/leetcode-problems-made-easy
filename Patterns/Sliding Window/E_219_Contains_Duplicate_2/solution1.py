class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        curr = 0
        hashmap = {}
        hashmap[nums[curr]] = 1
        if k < 1:
            return False
        for j in range(1, len(nums)):
            if nums[j] in hashmap and j - curr <= k:
                return True
            else:
                hashmap[nums[j]] = 1
            if j - curr >= k:
                hashmap.pop(nums[curr])
                curr += 1
        return False
