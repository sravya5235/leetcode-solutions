class Solution:
    def generate(self, numRows: int):
        res = []

        for i in range(numRows):
            if i == 0:
                res.append([1])
            else:
                prev = res[-1]
                row = [1]

                for j in range(1, len(prev)):
                    row.append(prev[j - 1] + prev[j])

                row.append(1)
                res.append(row)

        return res
