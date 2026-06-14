class Solution:
    # Precomputed C(n, k) % 5 for n, k < 5
    pascal_mod_5 = [
        [1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [1, 2, 1, 0, 0],
        [1, 3, 3, 1, 0],
        [1, 4, 1, 4, 1]
    ]

    def _get_lucas_mod5(self, n_val: int, k_val: int) -> int:
        """
        Calculates C(n_val, k_val) % 5 using Lucas's Theorem.
        """
        if k_val < 0 or k_val > n_val:
            return 0
        
        res = 1
        
        # Process digits in base 5
        while n_val > 0 or k_val > 0:
            n_digit = n_val % 5
            k_digit = k_val % 5
            
            # C(n, k) % p = PROD( C(n_i, k_i) % p )
            res = (res * self.pascal_mod_5[n_digit][k_digit]) % 5
            
            if res == 0:
                # If any C(n_i, k_i) is 0, the whole product is 0.
                break
                
            n_val //= 5
            k_val //= 5
            
        return res

    def hasSameDigits(self, s: str) -> bool:
        """
        Checks if the final two digits after all operations are the same.
        """
        n = len(s)
        if n == 2:
            return s[0] == s[1]
        
        # Convert string to a list of integers
        nums = [int(digit) for digit in s]
        
        # k = number of operations = n - 2
        k = n - 2
        # m = n - 1 (used for mod 2 check)
        m = n - 1

        # 1. Check Modulo 2
        # We check if (SUM(C(m, i) * d[i] for i=0..m)) % 2 == 0
        sum_mod2 = 0
        for i in range(n):  # i from 0 to m (which is n-1)
            # C(m, i) % 2 == 1 iff (m & i) == i (Lucas's Theorem for p=2)
            if (m & i) == i:
                sum_mod2 = (sum_mod2 + nums[i]) % 2
        
        if sum_mod2 != 0:
            # D0 % 2 != D1 % 2, so they can't be equal
            return False

        # 2. Check Modulo 5
        # We check if D0 % 5 == D1 % 5
        # D0 = (SUM(C(k, i) * d[i] for i=0..k)) % 5
        # D1 = (SUM(C(k, i) * d[i+1] for i=0..k)) % 5
        
        d0_mod5 = 0
        d1_mod5 = 0
        
        for i in range(k + 1):  # i from 0 to k
            # Get C(k, i) % 5 using Lucas's Theorem
            coeff_mod5 = self._get_lucas_mod5(k, i)
            
            if coeff_mod5 != 0:
                # Python's integers handle arbitrary precision
                d0_mod5 = (d0_mod5 + coeff_mod5 * nums[i]) % 5
                d1_mod5 = (d1_mod5 + coeff_mod5 * nums[i+1]) % 5

        if d0_mod5 != d1_mod5:
            # D0 % 5 != D1 % 5, so they can't be equal
            return False
        
        # 3. Final Result
        # If both mod 2 and mod 5 checks pass, then D0 % 10 == D1 % 10
        return True