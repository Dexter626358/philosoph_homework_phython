# Код начинается здесь ...
f = open("nums.txt")
n = f.read()
n = n.split()
for i in range(len(n)):
    n[i] = int(n[i])
print(sum(n))
