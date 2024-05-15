def factorial(a):
    result = 1
    for i in range(a, 0, -1):
        result *= i
    return result

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())

    ans = factorial(M) // (factorial(N) * factorial(M-N))

    print(ans)