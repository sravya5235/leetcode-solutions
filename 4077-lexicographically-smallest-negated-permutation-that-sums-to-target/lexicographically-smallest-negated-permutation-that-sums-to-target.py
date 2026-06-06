class Solution:
    def sumUpTo(self, x: int) -> int:
        return x * (x + 1) // 2

    def lexSmallestNegatedPerm(self, n: int, target: int) -> List[int]:
        S = self.sumUpTo(n)
        if target < -S or target > S:
            return []

        v = []
        for i in range(n, 0, -1):
            # Prefer -i if it's still possible to reach target with remaining numbers
            if self.sumUpTo(i - 1) - i >= target:
                target += i   # choose -i
                v.append(-i)
            else:
                target -= i   # choose +i
                v.append(i)

        if target != 0:
            return []

        v.sort()
        return v