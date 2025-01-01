class Solution(object):
    def maxOperations(self, nums, k):
        occ = {}
        op = 0

        for n in nums:
            if n < k:
                if k - n in occ and occ[k - n] > 0:
                    occ[k - n] -= 1
                    op += 1
                else:
                    if n in occ:
                        occ[n] += 1
                    else:
                        occ[n] = 1

        return op
