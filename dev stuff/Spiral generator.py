import sys

n = int(sys.argv[1])
for i in range(n):
    c = (i + (1 - n % 2) * (n / 2 <= i)) % 2
    a, b = [[(n - i) // 2] * 2, [-1 + c + i // 2, i // 2 + c]][i * 2 < n]
    print("##  " * a + 2 * "# "[c] * (n - 2 * [0, a][a >= 1] - 2 * b) + '  ##' * b)
