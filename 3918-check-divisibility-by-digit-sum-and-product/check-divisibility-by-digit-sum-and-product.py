class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum = 0
        digit_prod = 1
        orig = n
        while n > 0:
            rem = n % 10
            digit_sum = digit_sum + rem 
            digit_prod = digit_prod * rem
            n //= 10
        total_sum = digit_sum + digit_prod
        return orig % total_sum == 0