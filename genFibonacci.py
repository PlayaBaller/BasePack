fibonacci_numb = [0, 1]

for i in range(2, 700):
    fibonacci_numb.append(fibonacci_numb[i-1]+fibonacci_numb[i-2])
    print(fibonacci_numb)

print(sum(x for x in fibonacci_numb if x < 4000000 and x % 2 == 0))
# 4613732



