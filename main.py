import datetime

class Fornecedor:
 def __init__(self, nome, descricao_servico, data_vencimento, valor_pagar):
 self.nome = nome
 self.descricao_servico = descricao_servico
 self.data_vencimento = datetime.datetime.strptime(data_vencimento, "%d/%m/%Y")
 self.valor_pagar = float(valor_pagar)

 def __str__(self):
 return f"Fornecedor: {self.nome}\nDescrição do Serviço: {self.descricao_servico}\nData de Vencimento: {self.data_vencimento.strftime('%d/%m/%Y')}\nValor a Pagar: R${self.valor_pagar:.2f}"

class CadastroFornecedor:
 def __init__(self):
 self.fornecedores = []

 def cadastrar_fornecedor(self):
 nome = input("Digite o nome do fornecedor: ")
 descricao_servico = input("Digite a descrição do serviço: ")
 data_vencimento = input("Digite a data de vencimento (dd/mm/aaaa): ")
 valor_pagar = input("Digite o valor a pagar: ")
 fornecedor = Fornecedor(nome, descricao_servico, data_vencimento, valor_pagar)
 self.fornecedores.append(fornecedor)
 print("Fornecedor cadastrado com sucesso!")

 def listar_fornecedores(self):
 for fornecedor in self.fornecedores:
 print(fornecedor)
 print("------------------------")

 def buscar_fornecedor(self):
 nome = input("Digite o nome do fornecedor a buscar: ")
 for fornecedor in self.fornecedores:
 if fornecedor.nome.lower() == nome.lower():
 print(fornecedor)
 return
 print("Fornecedor não encontrado.")

 def pagar_fornecedor(self):
 nome = input("Digite o nome do fornecedor a pagar: ")
 for fornecedor in self.fornecedores:
 if fornecedor.nome.lower() == nome.lower():
 print(f"Valor a pagar: R${fornecedor.valor_pagar:.2f}")
 confirmar = input("Deseja pagar? (s/n): ")
 if confirmar.lower() == "s":
 fornecedor.valor_pagar = 0
 print("Pagamento realizado com sucesso!")
 return
 print("Fornecedor não encontrado.")

def main():
 cadastro = CadastroFornecedor()
 while True:
 print("1. Cadastrar Fornecedor")
 print("2. Listar Fornecedores")
 print("3. Buscar Fornecedor")
 print("4. Pagar Fornecedor")
 print("5. Sair")
 opcao = input("Digite a opção: ")
 if opcao == "1":
 cadastro.cadastrar_fornecedor()
 elif opcao == "2":
 cadastro.listar_fornecedores()
 elif opcao == "3":
 cadastro.buscar_fornecedor()
 elif opcao == "4":
 cadastro.pagar_fornecedor()
 elif opcao == "5":
 break
 else:
 print("Opção inválida.")

if __name__ == "__main__":
 main()
