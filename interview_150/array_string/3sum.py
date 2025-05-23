class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        len_nums = len(nums)
        answers = []
        nums.sort()

        for i in range(len_nums - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len_nums - 1
            while k > j:
                if nums[i] + nums[j] + nums[k] == 0:
                    answers.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1

        return answers