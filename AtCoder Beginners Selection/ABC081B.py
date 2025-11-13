n = input()
a = list(map(int, input().split()))

count = 0
while all(i % 2 == 0 for i in a):
    a = [j // 2 for j in a]
    count += 1

print(count)
