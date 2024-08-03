def find_max_product_pair(N, A):
    max_product = float('-inf')
    result_pair = []
    for i in range(N):
        for j in range(N):
            if i != j and A[i] + A[j] == 18 and A[i] > A[j]:
                product = A[i] * A[j]
                if product > max_product:
                    max_product = product
                    result_pair = [A[i], A[j]]

    return result_pair

n=int(input())
a=list(map(int,input().split()))
print(find_max_product_pair(n, a))