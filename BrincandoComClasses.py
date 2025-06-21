import os

# =========================
# Classe
# =========================
class Filme:
    def __init__(self, titulo, genero, ano):
        self.titulo = titulo
        self.genero = genero
        self.ano = ano
        self.assistido = False

    def exibir_detalhes(self):
        print(f"{self.titulo}, {self.genero}, {self.ano}")
        print("Assistido" if self.assistido else "Não assistido")

    def checar_assistido(self):
        if self.assistido:
            print(f"{self.titulo} já foi assistido.")
            return False
        else:
            print(f"{self.titulo} ainda não foi assistido, deseja marcar?")
            return True

    def marcar_assistido(self):
        print(f"Marcando {self.titulo} como assistido...")
        self.assistido = True

# =========================
# Funções para manipular a lista de filmes
# ========================

lista_de_filmes = []

def limpar_tela():
    os.system('cls')
    print("\nTela limpa!\n")

def adicionar_filme(lista):
    print("\n--- Adicionar Filme ---\n")
    try:
        nome = input("Nome do filme: ")
        genero = input("Gênero do filme: ")
        ano = input("Ano do filme: ")
        novo_filme = Filme(nome, genero, int(ano))
        if verificar_filme_lista(lista, novo_filme):
            lista.append(novo_filme)
            print("\nFilme adicionado com sucesso!\n")
    except ValueError:
        print("\nErro: O ano deve ser um número válido\n")

def verificar_filme_lista(lista, novo_filme):
    for filme in lista:
        if filme.titulo == novo_filme.titulo:
            print("Filme já na lista")
            return False
    return True

def listar_filmes():
    limpar_tela()
    print("\n--- Lista de Filmes ---\n")
    if not lista_de_filmes:
        print("Não há filmes para listar.\n")
        return
    for filme in lista_de_filmes:
        filme.exibir_detalhes()
        print()

def marcar_assistido():
    if not lista_de_filmes:
        print("\nNão há filmes na lista!\n")
        return
    print("\n--- Marcar Filme como Assistido ---\n")
    for n, filme in enumerate(lista_de_filmes):
        print(f"{n}: {filme.titulo}")
    filme_marcar_assistido = input("\nQual filme deseja marcar como assistido? ").strip().lower()
    filme_encontrado = False
    for filme in lista_de_filmes:
        if filme_marcar_assistido == filme.titulo.strip().lower():
            filme.assistido = True
            print(f"\n{filme.titulo} marcado como assistido!\n")
            filme_encontrado = True
            break
    if not filme_encontrado:
        print("\nFilme não encontrado na lista!\n")

def sair():
    global executando
    print("\nSaindo do programa...\n")
    executando = False
    return executando

# =========================
# Menu principal
# =========================

opcoes = {
    '1': lambda: adicionar_filme(lista_de_filmes),
    '2': listar_filmes,
    '3': marcar_assistido,
    '4': sair,
    '5': limpar_tela,
}

executando = True
while executando:
    print("\n=== Menu de Opções ===")
    print("1: Adicionar filme | 2: Listar filmes | 3: Marcar como assistido | 4: Sair | 5: Limpar tela")
    opcao = input("\nEscolha uma opção: ").strip()

    comando = opcoes.get(opcao)
    if comando:
        comando()
    else:
        print("\nComando inválido! Por favor, escolha uma opção de 1 a 5.\n")
