num_inicial=int(input("diga o numero inicial"))
num_final= int(input("Diga o numero final"))
incremento=int(input("incremento"))

print(f"os números entre{num_inicial} e{num_final} com incremento de {incremento}")
for i in range(num_inicial,num_final +  1,incremento):
    print(i)