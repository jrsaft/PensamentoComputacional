from models.Conta import Conta
Banco = [] # Criando a lista.
Banco.append(Conta("Brenda", 600, 100, [])) # Adicionando usuários.
Banco.append(Conta("Joana", 400, 800, [])) # Adicionando usuários.  

while True:
    print( "Para Criar um cadastro, digite 0."
      "\nPara sacar, digite 1"
      "\nPara depositar, digite 2" +
      "\nPara transferir, digite 3" +
      "\nPara consultar o saldo, digite 4" +
      "\nPara excluir uma conta, digite 5" +
      "\nPara mostrar as contas do Banco, digite 6" +
      "\nPara exibir histórico, digite 7" +
      "\nPara encerrar, digite sair.")
    op = input("Digite o número da operação que deseja realizar: [0, 1, 2, 3, 4, 5 ou sair para encerrar]")
    if op == "sair":
       break
    if op == "0":
      nome = input("Qual o nome do titular da conta de cadastro?")
      saldot = float(input("Qual o saldo do titular da conta de cadastro?"))
      Banco.append(Conta(nome, saldot, "", []))
      print("A conta de", nome,"foi adicionada com sucesso!")
    if op == "1":
        titularsaque = input("Quem deseja realizar um saque?")
        valorsaque = float(input("De quanto será o saque?"))
        for conta in Banco:
            if conta.titular == titularsaque:
                conta.sacar(valorsaque)
                print(f"O saldo de",titularsaque,"é: R$:",conta.saldo)
    elif op == "2":
      titulardeposito = input("Quem deseja realizar um depósito?")
      valordeposito = float(input("De quanto será o depósito?"))
      for conta in Banco:
        if conta.titular == titulardeposito:
          conta.depositar(valordeposito)
          print(f"O saldo de",titulardeposito,"é: R$:",conta.saldo)
    elif op == "3":
        remetentetrans = input("Quem enviará a transferência?")
        valordeposito = float(input("De quanto será a transferência?"))
        destinatariotransf = input("Quem receberá a transferência?")
        remetente = next((c for c in Banco if c.titular == remetentetrans), None)
        destinatario = next((c for c in Banco if c.titular == destinatariotransf), None)
        if remetente and destinatario:
            remetente.transferencia(destinatario, valordeposito)
            print(f"{remetentetrans} enviou R${valordeposito} para {destinatariotransf}")
        else:
            print("Remetente ou destinatário não encontrado.")
    elif op == "4":
        titular = input("Digite o titular da conta que deseja ver o saldo:")
        encontrou = False
        for conta in Banco: 
            if conta.titular == titular:
                print(f"O", titular,"tem R$",conta.saldo,"em conta!") 
                encontrou = True
        if not encontrou:
           print("Conta não encontrada.") 
    elif op == "6":
       for conta in Banco:
          print(f"titular:{conta.titular}, saldo:{conta.saldo}") 
    elif op == "7":
        pessoa = input("Deseja exibir o histórico de qual titular? ")
        encontrou = False
        for conta in Banco:
            if conta.titular == pessoa:
                conta.exibirhistorico()
                encontrou = True
                break
        if not encontrou:
            print("Conta não encontrada.")
    else:
        op == "5"
        cancelado = input("Qual o nome do titular da conta de cadastro?")
        encontrou = False
        for conta in Banco:
            if conta.titular == cancelado:
                Banco.remove(conta)
                encontrou = True
                print(f"Conta de {cancelado} removida com sucesso.")
        if not encontrou:
           print("Conta não encontrada.")             


