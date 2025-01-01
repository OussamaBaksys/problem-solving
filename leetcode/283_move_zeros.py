class Solution(object):
    def moveZeroes(self, nums):
        index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[index] = nums[i]
                if i != index:
                    nums[i] = 0
                index += 1
        return nums