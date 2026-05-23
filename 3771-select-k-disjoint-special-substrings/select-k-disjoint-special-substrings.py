class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        first = {}
        last = {}
        count = Counter()
        for i,c in enumerate(s):
            first.setdefault(c, i)
            last[c] = i
            count[c] += 1

        intervals = []
        for c1,i in first.items():
            for c2,j in last.items():
                if i <= j:
                    cnt = 0
                    for c in count:
                        if i <= first[c] <= last[c] <= j:
                            cnt += count[c]
                    if cnt == j - i + 1 and cnt < len(s):
                        intervals.append([i, j])

        intervals.sort(key = lambda s: s[1] - s[0])
        res = []
        for i,j in intervals:
            if all(y < i or j < x for x,y in res):
                res.append([i, j])
        return len(res) >= k