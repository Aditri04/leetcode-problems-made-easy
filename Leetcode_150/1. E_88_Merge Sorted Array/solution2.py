class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_cnt = m-1
        nums2_cnt = n-1
        while nums1_cnt+nums2_cnt > -2 and nums2_cnt>-1:
            if nums1_cnt>-1 and nums1[nums1_cnt]>nums2[nums2_cnt]:
                nums1[nums1_cnt+nums2_cnt+1] = nums1[nums1_cnt]
                nums1_cnt-=1
            else:
                nums1[nums1_cnt+nums2_cnt+1] = nums2[nums2_cnt]
                nums2_cnt-=1