nilai = input("Input nilai: ").split()

a = 0
for b in range(0, len(nilai)):
    nilai[b] = int(nilai[b])

for c in nilai:
    if c > a:
        a = c

print(a)
