import re

class Solution:
    def validateCoupons(self, code, businessLine, isActive):
        n = len(code)
        valid_lines = {"electronics", "grocery", "pharmacy", "restaurant"}
        order = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}

        pattern = re.compile(r"^[A-Za-z0-9_]+$")
        res = []

        for i in range(n):
            if not pattern.match(code[i]): 
                continue
            if businessLine[i] not in valid_lines:
                continue
            if not isActive[i]:
                continue
            
            res.append((businessLine[i], code[i]))

        res.sort(key=lambda x: (order[x[0]], x[1]))
        return [c for _, c in res]
