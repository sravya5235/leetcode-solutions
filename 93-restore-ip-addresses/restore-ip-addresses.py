class Solution:
    def restoreIpAddresses(self, s: str):
        res = []

        def valid(part):
            if len(part) > 1 and part[0] == '0':
                return False
            return 0 <= int(part) <= 255

        def backtrack(start, path):
            if len(path) == 4:
                if start == len(s):
                    res.append(".".join(path))
                return

            for l in range(1, 4):
                if start + l > len(s):
                    break
                part = s[start:start + l]
                if valid(part):
                    backtrack(start + l, path + [part])

        backtrack(0, [])
        return res 