class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        right_max = height[right]
        left_max = height[left]
        water = 0

        while right > left:
            if right_max > left_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]
        print(water)