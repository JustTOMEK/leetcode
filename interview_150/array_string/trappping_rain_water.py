heights = [2, 1, 0, 1, 3, 2, 3]
left = 0
right = len(heights) - 1
right_max = heights[right]
left_max = heights[left]
water = 0

while right > left:
    if right_max > left_max:
        left += 1
        left_max = max(left_max, heights[left])
        water += left_max - heights[left]
    else:
        right -= 1
        right_max = max(right_max, heights[right])
        water += right_max - heights[right]
print(water)