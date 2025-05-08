from models.Conta import Conta

Banco = [] # Criando a lista.

Banco.append(Conta("Brenda", 600, 100, [])) # Adicionando usuários.

Banco.append(Conta("Joana", 400, 800, [])) # Adicionando usuários. 

for conta in Banco: # Mostrando o titular da conta e seu saldo.
    print(f"Titular da conta:", conta.titular, ", Saldo:",conta.saldo)

titular = input("Digite o titular da conta que deseja ver o saldo:")
for conta in Banco: 
    if conta.titular == titular:
        print(f"O", titular,"tem R$",conta.saldo,"em conta!")
    

titularsaque = input("Quem deseja realizar um saque?")
valorsaque = float(input("De quanto será o saque?"))
for conta in Banco:
    if conta.titular == titularsaque:
        conta.sacar(valorsaque)
        print(f"O saldo de",titularsaque,"é: R$:",conta.saldo)

