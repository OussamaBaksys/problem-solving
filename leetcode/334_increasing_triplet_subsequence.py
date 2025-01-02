class Solution(object):
    def increasingTriplet(self, nums):
        if len(nums) < 3:
            return False
        first = float('inf')
        second = float('inf')
        for number in nums:
            if number <= first:
                first = number
            elif number <= second:
                second = number
            else:
                return True
        return False
