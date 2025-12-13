class Solution:
    def validateCoupons(self, code, businessLine, isActive):
        n = len(code)
        valid_lines = {"electronics", "grocery", "pharmacy", "restaurant"}
        order = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}

        res = []

        for i in range(n):
            c = code[i]
            b = businessLine[i]

            # Check code: non-empty & alphanumeric + underscore only
            if not c or any(not (ch.isalnum() or ch == "_") for ch in c):
                continue

            # Valid business line?
            if b not in valid_lines:
                continue

            # Must be active
            if not isActive[i]:
                continue

            res.append((b, c))

        # Sort by businessLine priority then lexicographically by code
        res.sort(key=lambda x: (order[x[0]], x[1]))

        # Return only codes
        return [c for _, c in res]
