class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        result = 0
        for key, value in count.items():
            if value == 2:   
                result ^= key
        return result


            
