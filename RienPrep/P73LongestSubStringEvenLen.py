def long_even_len_sub(n, s):
    maxlen = 0
    for le in range(2, n + 1, 2):
        for i in range(n - le + 1):
            sub = s[i:i + le]
            k = le // 2
            left_sum = sum(int(digit) for digit in sub[:k])
            right_sum = sum(int(digit) for digit in sub[k:])
            if left_sum == right_sum:
                maxlen = max(maxlen, le)
    return maxlen


n = int(input())
s = input()
print(long_even_len_sub(n, s))
