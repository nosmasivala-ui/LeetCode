class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        sum1, sum2 = 0, 0
        for num in nums:
            new_sum = max(sum1, sum2 + num)
            sum2, sum1 = sum1, new_sum

        return sum1

