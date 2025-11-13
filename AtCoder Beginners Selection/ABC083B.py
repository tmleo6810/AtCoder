n, a, b = (int(x) for x in input().split())
sum_of_all = 0

for i in range(n):
    sum_of_digit = sum(map(int, str(i+1)))
    if a <= sum_of_digit <= b:
        sum_of_all += i+1

print(sum_of_all)
