class Solution:
    def maxArea(self, height: List[int]) -> int:
        right = len(height) - 1
        left = 0
        max_water = 0

        while right > left:
            if (right - left) * min(height[left], height[right]) > max_water:
                max_water = (right - left) * min(height[left], height[right])
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water