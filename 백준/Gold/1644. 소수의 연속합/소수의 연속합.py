import sys

N = int(sys.stdin.readline())

#N까지의 소수 찾기 (에라토스테네스 체)
prime_number = [True for i in range(N+1)]
p = 2
while p*p <= N:
    if prime_number[p] == True:
        for i in range(p*p, N+1, p):
            prime_number[i] = False
    p += 1
primes = [i for i in range(2, N+1) if prime_number[i]]

#연속된 소수의 합으로 타겟을 구할 수 있는지 
end = 0
sum = 0
count = 0
for start in range(len(primes)):
    while sum < N and end < len(primes):
        sum += primes[end]
        end += 1
    if sum == N:
        count += 1
    sum -= primes[start]

print(count)