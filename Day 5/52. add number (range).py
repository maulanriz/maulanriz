
a = 0
for number in range(2, 101, 2):
    a += number
print(a)

a2 = 0
for number in range(1,101):
    if number % 2 == 0:
        a2 += number
print(a2)