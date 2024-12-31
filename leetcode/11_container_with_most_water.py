class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        area = 0
        while (right > left):
            h = height[left] if height[left] < height[right] else height[right]
            l = right - left
            if area < h * l:
                area = h * l
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return area
