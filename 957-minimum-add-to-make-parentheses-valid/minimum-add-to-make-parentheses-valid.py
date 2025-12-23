class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0  # number of unmatched '('
        add = 0      # number of '(' to insert

        for ch in s:
            if ch == '(':
                balance += 1
            else:
                if balance > 0:
                    balance -= 1
                else:
                    add += 1  # need to insert '('

        return add + balance
