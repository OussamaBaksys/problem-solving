class Solution(object):
    def findDifference(self, nums1, nums2):
        d1 = set(nums1)
        d2 = set(nums2)
        return [list(d1 - d2), list(d2 - d1)]
