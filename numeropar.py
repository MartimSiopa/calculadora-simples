
num_inicial=int(input("diga o numero inicial"))
num_final= int(input("Diga o numero final"))



decisao= input("Par (P) Impar (I)")
if decisao == "P":
    if num_inicial%2==0:
        for i in range(num_inicial,num_final + 1,2):
            print(i)
    else:
        for i in range(num_inicial+1, num_final + 1,2):
            print(i)
elif decisao == "I":
    if num_inicial%2 != 0:
        for i in range(num_inicial + 1, num_final + 1,2):
            print(i)
    else:
        for i in range(num_inicial+1, num_final + 1,2):
            print(i)