file = open('docs/app.conf', 'r')
line = file.readline()
file.close()

a, b, c = line.split(" ")
a, b, c = int(a), int(b), int(c)
print(a, b, c)
arr = []
for i in range(a):
    arr.append(b*i + c)

print(arr)

