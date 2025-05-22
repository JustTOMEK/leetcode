class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dicto = {}
        maks = 0
        to_return = 0
        for element in nums:
            if element not in dicto:
                dicto[element] = 1
            else:
                dicto[element] += 1
            if dicto[element] > maks:
                maks = dicto[element]
                to_return = element
        return to_return