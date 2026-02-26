class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0
        
        # Traverse from right to left (ignore first bit)
        for i in range(len(s) - 1, 0, -1):
            bit = int(s[i])
            
            if bit + carry == 1:
                # Odd → +1 then /2
                steps += 2
                carry = 1
            else:
                # Even → /2
                steps += 1
        
        # If carry remains after processing MSB
        return steps + carry