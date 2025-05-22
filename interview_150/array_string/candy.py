class Solution:
    def candy(self, ratings: List[int]) -> int:
        number_of_kids = len(ratings)
        candies = [1] * number_of_kids

        for i in range(1, number_of_kids):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in range(number_of_kids - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                if candies[i] <= candies[i + 1]:
                    candies[i] = candies[i + 1] + 1
        return sum(candies)
