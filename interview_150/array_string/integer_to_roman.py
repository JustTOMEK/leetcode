class Solution:
    def intToRoman(self, num: int) -> str:
        dictionary = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        s = ''
        power = 1
        while num > 0:
            number = num%10
            if number == 4:
                s += dictionary [power * 5]
                s += dictionary[power]
            elif number == 9:
                s += dictionary[power * 10]
                s += dictionary[power]
            else:
                for i in range(number % 5):
                    s +=dictionary[power]
                if number >= 5:
                    s+= dictionary[power * 5]
                    number -= 5
            num = num // 10
            power*=10
        return s[::-1]