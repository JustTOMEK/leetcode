class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        possible_endings = []
        possible_water = []
        for start in range(0, n):
            max_end = start
            water = 0
            for end in range(start + 1, n):
                if height[end] >= height[start]:
                    max_end = end
                    break
                water += height[start] - height[end]
            possible_endings.append(max_end)
            possible_water.append(water)

        print(possible_endings)
        print(possible_water)
        water = 0
        current_index = 0
        while n>current_index:
            if possible_endings[current_index] - current_index >= 2:
                water += possible_water[current_index]
            if possible_endings[current_index] == current_index:
                current_index += 1
            else:
                current_index = possible_endings[current_index]
        print(water)

