
import time # para salvar a data e horário da transação
class Conta:
    '''
    Classe que implementa métodos para manipular uma conta bancária
    Atributos: titular(str), saldo (float), limite (float) e históricos (lista de dicionários)

    OBS: Operações no histórico: 0 - sacar, 1 - depositar, 2 - transferir, 3 - pix
    '''
    
    def __init__(self, titular, saldo, limite, historico):
        self.titular = titular
        self.saldo =  saldo
        self.limite = limite
        self.historico = historico

    def depositar(self, valor, remetente = ""): # None para não dar erro.
        op = 1
        if remetente != None:
            op= 2 # transferencia
        if valor > 0: # Conferindo se o número é negativo
            self.saldo = self.saldo + valor 
            self.historico.append({"operacao": op,
                                    "remetente": remetente,
                                    "destinatario": self.titular,
                                    "valor": valor,
                                    "saldo": self.saldo,
                                    "dataetempo": int(time.time())}) #Adicionando a transação ao histórico da conta
            return True
        else:
            print("O valor é inválido")
            return False

    def sacar(self, valor, destinatario = None):
        op = 0
        if destinatario != None:
            op= 2 # transferencia
        if valor <= self.saldo:
            self.saldo = self.saldo - valor
            self.historico.append({"operacao": op,
                                    "remetente": self.titular,
                                     "destinatario": destinatario,
                                     "valor": valor,
                                     "saldo": self.saldo,
                                     "dataetempo":int(time.time())}) #Adicionando a transação ao histórico da conta
        else: # caso não tenha dinheiro suficiente 
            a = input(f"Deseja utilizar seu limite de crédito?") 
            if a == "s": 
                if (self.saldo + self.limite) >= valor: #Calculando se há limite disponível
                    self.saldo -= valor
                    print ("Saque realizado!")
                    return True
                else:
                    print("Saldo e limite insuficiente!")
            else: #Não quer mexer no limite
                print("Operação com limite cancelada!")
                return False
                
    def exibirhistorico(self):
        print("Histórico de transação:")
        for transacao in self.historico:
            dt = time.localtime(transacao["dataetempo"]) # associando a biblioteca de data e tempo
            print("Op:", transacao["operacao"], 
                  ", Remetente:", transacao["remetente"],
                  ", Destinatário:", transacao["destinatario"], 
                  ", Saldo:", transacao["saldo"],
                  ", Valor:", transacao["valor"],
                  ", Data e tempo:", str(dt.tm_hour) + ":" + str(dt.tm_min)
                  + ":" + str(dt.tm_sec) + " " + str(dt.tm_mday) + "/" + str(dt.tm_mon) + "/" + str(dt.tm_year))
                # utilizando de cada item do localtime
            
    def transferencia(self, destinatario, valor):
        if self.sacar(valor, destinatario.titular):
            destinatario.depositar(valor, self.titular)
            return True
        return False
    def pix(self, destinatario, valor):
        op = "3"
        if valor >= 0:
            if valor <= self.saldo:
                self.sacar(valor)
                self.historico.append({"operacao": op,
                                    "remetente": self.titular,
                                     "destinatario": destinatario,
                                     "valor": valor,
                                     "saldo": self.saldo,
                                     "dataetempo":int(time.time())})
                destinatario.depositar(valor)
                destinatario.historico.append({"operacao": op,
                                    "remetente": self.titular,
                                     "destinatario": destinatario,
                                     "valor": valor,
                                     "saldo": self.saldo,
                                     "dataetempo":int(time.time())})
                print("Pix realizado")


        
