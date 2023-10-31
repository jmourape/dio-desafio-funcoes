vitorias = int(input("Qual a quantidade de vitorias? "))
derrotas = int(input("Qual a quantidade de derrotas? "))
saldo = vitorias - derrotas
if(saldo <= 10):
    nivel = "Ferro"
elif(saldo <= 20):
    nivel = "Bronze"
elif(saldo <= 50):
    nivel = "Prata"
elif(saldo <= 80):
    nivel = "Ouro"
elif(saldo <= 90):
    nivel = "Diamante"
elif(saldo <= 100):
    nivel = "Lendário"
else:
    nivel = "Imortal"
print(f"O Herói tem de saldo de {saldo} vitórias e está no nível de {nivel}")