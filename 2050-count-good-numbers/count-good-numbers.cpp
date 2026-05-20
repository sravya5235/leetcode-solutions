class Solution {
public:
    long long MOD = 1e9 + 7;
    long long binary_exp(long long a, long long n) {
        long long res = 1;
        while (n > 0) {
            if (n & 1) res = (res * a) % MOD;
            a = (a * a) % MOD;
            n /= 2;
        }
        return res;
    }

    int countGoodNumbers(long long n) {
        long long o = n / 2;
        long long e = n - o;
        long long res = (binary_exp(4, o) * binary_exp(5, e)) % MOD;
        return (int) res;
    }
};