class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        ans = []
        k = celsius + 273.15
        ans.append(k)
        f = celsius * 1.80 + 32.00
        ans.append(f)
        return ans