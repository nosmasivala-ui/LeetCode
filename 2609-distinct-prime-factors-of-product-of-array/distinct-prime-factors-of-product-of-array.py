class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        prod = 1
        for i in range(len(nums)):
            prod *= nums[i]

        s = []
        while prod % 2 == 0:
            s.append(2)
            prod //= 2

        i = 3
        while i * i <= prod:
            while prod % i == 0:
                s.append(i)
                prod //= i
            i += 2

        if prod > 2:
            s.append(prod)
        
        return len(set(s))