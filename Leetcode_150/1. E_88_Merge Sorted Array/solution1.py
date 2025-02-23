class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        cnt1 = m-1
        cnt2 = n-1
        cnt3= m+n-1
        if n >0:
            while True:
                if cnt1 <0:
                    nums1[cnt3] = nums2[cnt2]
                    cnt2 -=1
                    cnt3 -=1
                else:
                    if nums1[cnt1]>nums2[cnt2]:
                        nums1[cnt3] = nums1[cnt1]
                        cnt1-=1
                        cnt3-=1
                    else:
                        nums1[cnt3] = nums2[cnt2]
                        cnt2-=1
                        cnt3-=1
                if cnt2 == -1:
                    break