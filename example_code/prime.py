# declaration or setting parameters
i = 1
list = [i for i in range(3, 400, 2)]
p = [2, 3]
#print(list)

while True:
    while p[len(p) - 1] * i < max(list):
        i = i + 1
        if p[len(p) - 1] * i in list:
            list.remove(p[len(p) - 1] * i)
    i = 1
    list.remove(list[0])
    p.append(list[0])
    if len(list) == 1:
        break
#print(list)
print("Prime numbers:",p)
