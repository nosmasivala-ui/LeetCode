class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        profit = 0
        min_price = nums[0]
        
        for i in range(len(nums)):
            if nums[i] <= min_price:
                min_price = nums[i]   
            else:
                n = nums[i] - min_price
                if n > profit:
                    profit = n
                    
        return profit


                

