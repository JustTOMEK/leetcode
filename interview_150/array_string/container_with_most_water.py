class Solution:
    def maxArea(self, height: List[int]) -> int:
        right = len(height) - 1
        left = 0
        right_max = height[right]
        left_max = height[left]
        max_water = 0

        while right > left:
            if (right - left) * min(height[left], height[right]) > max_water:
                max_water = (right - left) * min(height[left], height[right])
            if right_max > left_max:
                left += 1
                left_max = max(left_max, height[left])
            else:
                right -= 1
                right_max = max(right_max, height[right])
        return max_water