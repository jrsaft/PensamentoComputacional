from models.Conta import Conta

conta1 = Conta("Guilherme", 1000, 500, [])
conta2 = Conta("Julia", 2, 7000, [])

conta1.depositar(150)
conta1.sacar(100)
conta1.exibirhistorico()