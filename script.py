d=int(input("diz um número:"))
e=int(input("diz outro número:"))
sinal=input("diz um sinal como:*+-/:")
if sinal =="+":
    f = d + e
elif sinal == "-":
    f = d - e
if sinal == "*":
    f = d * e
elif sinal == "/":
    f = d / e
print(f)