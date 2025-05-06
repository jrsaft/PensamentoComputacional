class Conta:
    def __init__(self, titular, saldo, limite, historico):
        self.titular = titular
        self.saldo =  saldo
        self.limite = limite
        self.historico = historico

    def depositar(self, valor):
    if valor > 0: # Conferindo se o número é negativo
        self.saldo = self.saldo + valor 
    else:
        print("O valor é inválido")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo = self.saldo - valor
            self.historico.append() #Adicionando a transação ao histórico da conta
        else: # caso não tenha dinheiro suficiente 
            a = input(f"Deseja utilizar seu limite de crédito?") 
            if a == "s": 
                if (self.saldo + self.limite) >= valor: #Calculando se há limite disponível
                    self.saldo -= valor
                    print ("Saque realizado!")
                else:
                    print("Saldo e limite insuficiente!")
            else: #Não quer mexer no limite
                print("Operação com limite cancelada!")

                
