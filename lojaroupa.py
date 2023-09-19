import os
class Produto:
    def _init_(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Carrinho:
    def _init_(self):
        self.produtos = []

    def adicionar_produto(self, produto, quantidade):
        self.produtos.append({'produto': produto, 'quantidade': quantidade})

    def calcular_total(self):
        total = 0
        for item in self.produtos:
            total += item['produto'].preco * item['quantidade']
        return total

class Cliente:
    def _init_(self, nome, email):
        self.nome = nome
        self.email = email

class Pedido:
    def _init_(self, cliente):
        self.cliente = cliente
        self.carrinho = Carrinho()

    def adicionar_produto(self, produto, quantidade):
        self.carrinho.adicionar_produto(produto, quantidade)

    def calcular_total_pedido(self):
        return self.carrinho.calcular_total()
    os.system('cls')


def menu():
    while True:
        print("\n====== PowerLift Athletic Wear ======")
        print("1. COMPRE SEU PRODUTO ")
        print("2. FAÇA SEU CADASTRO ")
        print("3. FINALIZE SEU PEDIDO ")
        print("4. SAIR ... ")
        escolha = input(" >>> ")
        os.system('cls')
        

        if escolha == '1':
            comprar_produto()
            
        elif escolha == '2':
            cadastrar_cliente()
        elif escolha == '3':
            finalizar_pedido()
        elif escolha == '4':
            print(" ÓTIMA ESCOLHA EM COMPRAR NA POWERLIFT ATHLETIC WEAR \n  ATÉ A PROXIMA!! ")
            break
        else:
            print("Opção inválida!! \n Tente novamente!! \n ")

clientes = []
pedidos = []

def comprar_produto():
    print("\n===== DISPONIVEIS =====")
    for i, produto in enumerate(produtos, 1):
        print(f"{i}. {produto.nome} - Preço: R${produto.preco}")
        


    escolha = int(input(" ==== ESCOLHA O PRODUTO DE ACORDO COM A NUMERAÇÃO ==== "))
    os.system('cls')
    quantidade = int(input(" quantidade desejada... "))
    
    if 1 <= escolha <= len(produtos):
        produto = produtos[escolha - 1]

        
    else:
        print("ERRO INESPERADO")
        pedido_atual.adicionar_produto(produto, quantidade)
        print(f"{quantidade} {produto.nome}(s) adicionado(s) ao seu carrinho!!")
        os.system('cls')




def cadastrar_cliente():
    nome = input("Nome do cliente: ")
    email = input("Email do cliente: ")
    cliente = Cliente(nome, email)
    clientes.append(cliente)
    os.system('cls')
    print(f"FOI CADASTRADO O {email} NA CONTA DE {nome}")

def finalizar_pedido():
    if not pedido_atual.carrinho.produtos:
        print("PARA FINALIZAR O PEDIDO O SEU CARRINHO DEVE ESTAR NO MINIMO COM 1 PRODUTO")
        return
    os.system('cls')
    total_pedido = pedido_atual.calcular_total_pedido()
    pedidos.append(pedido_atual)
    print(f"PEDIDO FINALIZADO!!")
    print(f"O VALOR TOTAL É DE R${total_pedido}")
    print(f" CLIENTE {pedido_atual.cliente.nome}")
    print("== PRODUTOS NO PEDIDO ==")
    for item in pedido_atual.carrinho.produtos:
        print(f"PRODUTO  {item['produto'].nome} \n   QUANTIDADE {item['quantidade']} \n    PREÇO UNITARIO R${item['produto'].preco}")
os.system('cls')
if _name_ == "__main__":
    produtos = [Produto("Straps Roxo", 209.99), Produto("Regata Preta Berserk", 49.99), Produto("Cinturão Agachamento", 99.99)]
    pedido_atual = None

    menu()
