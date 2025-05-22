class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dictio = {}
        counter = 0
        for element in nums:
            if element not in dictio:
                dictio[element] = 1
                nums[counter] = element
                counter += 1
            elif dictio[element] == 1:
                dictio[element] = 2
                nums[counter] = element
                counter += 1
        return counters