class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        
        for _ in range(32):
            result = (result << 1) | (n & 1)   # add last bit
            n >>= 1                            # remove last bit
        
        return result
