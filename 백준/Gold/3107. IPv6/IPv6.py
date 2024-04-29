import sys
input = sys.stdin.readline

address = input().rstrip().split(':')

if address.count(''):
    #생략된 경우가 맨 앞이나 뒤인 경우 ex)::1:2:3:4:5:6:7
    while len(address) > 8:
        address.remove('')
    while len(address) < 8:
        address.insert(address.index(''), '0000')

#
for i in range(8):
    if len(address[i]) < 4:
        address[i] = '0'*(4-len(address[i])) + address[i]

print(*address, sep=':')
