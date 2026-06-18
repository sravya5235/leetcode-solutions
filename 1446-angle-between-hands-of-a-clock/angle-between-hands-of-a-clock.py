class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        x = hour + minutes / 60
        difference = (11 * x) % 12
        return min(difference, 12 - difference) * 30