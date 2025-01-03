class Solution(object):
    def findMaxAverage(self, nums, k):
        new_sum = sum(nums[0:k])
        target = new_sum
        for i in range(1, len(nums) - k + 1):
            new_sum -= nums[i - 1]
            new_sum += nums[i + k - 1]
            if new_sum > target:
                target = new_sum
        return target / float(k)
