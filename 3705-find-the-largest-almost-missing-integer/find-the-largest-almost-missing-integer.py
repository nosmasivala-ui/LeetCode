class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == 1:
            freq = {}
            for num in nums:
                freq[num] = freq.get(num, 0) + 1
            candidates = [num for num, count in freq.items() if count == 1]
            return max(candidates) if candidates else -1

        if k == n:
            return max(nums)

        first, last = nums[0], nums[-1]
        count_first = nums.count(first)
        count_last = nums.count(last)

        candidates = []
        if count_first == 1:
            candidates.append(first)
        if count_last == 1:
            candidates.append(last)

        return max(candidates) if candidates else -1
