class Solution:
    def isUgly(self, n: int) -> bool:
        # f = []
        # m = []
        # for i in range(1,n + 1):
        #     if n % i == 0:
        #         f.append(i)
        # for i in range(2, int(math.sqrt(n)) + 1):
        #     if n % i != 0: 
        #         m.append(i)
        # if m in f:
        #     return False
        # return True

        if n <= 0:
            return False

        for p in [2, 3, 5]:
            while n % p == 0:
                n //= p

        return n == 1
