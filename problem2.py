#🟢 Problem 2: Sum of All Even Numbers from 1 to 100 ➕
sumEven = 0
for i in range(1, 101):
    if i % 2 == 0:
        sumEven += i
# or
# sumEven = sum(range(2, 101, 2))
print(sumEven)