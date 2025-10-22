int(input("quanto dinheiro queres emprestado?"))
divida= int(input("tem dividas? (1=sim 2=nao)"))

if divida==1:
    print("nao posso emprestar ")
elif divida==2:
    print("podemos emprestar",dinheiro,"€")
else:
    print("nao utilizaste a divida correta")
