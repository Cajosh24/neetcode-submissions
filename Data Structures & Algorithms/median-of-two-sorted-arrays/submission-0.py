class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_index = (len(nums1)+len(nums2))
        median_index = (total_index - 1) // 2

        nums3 = sorted(nums1 + nums2)

        if total_index % 2 == 0:
            return (nums3[median_index] + nums3[median_index + 1]) / 2
        else:
            return nums3[median_index]
        