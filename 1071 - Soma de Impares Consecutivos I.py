#Não resolvido
x = int(input())
y = int(input())
soma = 0
if x < y:
    for i in range(x+1, y-1):
        if i > 0:
            soma += i
else:
    for i in range(y+1, x-1):
        if i > 0:
            soma += i
print("{}".format(soma))