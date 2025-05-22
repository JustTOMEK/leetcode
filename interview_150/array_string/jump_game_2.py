class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        l = 0
        r = 0
        while len(nums) - 1 > r:
            max_jump = 0
            for i in range(l, r + 1):
                if i + nums[i] > max_jump:
                    max_jump = i + nums[i]
            l = r + 1
            r = max_jump
            jumps += 1
        return jumps

