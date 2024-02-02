class Solution:
    def fib(self, n: int) -> int:
        seq = [0, 1]
        if n <= 1:
            return n
        for i in range(2, n+1):
            seq.append(seq[i-1] + seq[i-2])
        return seq[-1]