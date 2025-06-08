
from functools import reduce
from itertools import groupby
import json
with open('produtos.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)
    vendas_lista = dados['produtos']
def filtrar_maiores_vinte(produto):
    return produto['preco'] > 20

def atualizar_precos(produto):
    return {
        'nome':produto['nome'],
        'categoria':produto['categoria'],
        'preco': produto['preco'] * 0.9
    }

def somar_valores(total,produto):
    print(f"{produto['nome']} adicionado, valor {round(produto['preco'],2)}")
    total += produto['preco']
    return total

produtos_filtrados_por_preco = filter(filtrar_maiores_vinte, vendas_lista)
produtos_com_desconto = map(atualizar_precos, produtos_filtrados_por_preco)
produtos_organizados = sorted(produtos_com_desconto,key=lambda v:v['categoria'])
produtos_em_grupos = groupby(produtos_organizados,key=lambda c:c['categoria'])
for grupo,produto in produtos_em_grupos:
    print(f"{'-' * 10}{grupo}{'-' * 10}")
    total = 0
    for p in produto:
        print (p['nome'],round(p['preco'],2))
        total += p['preco']
    print(f"TOTAL DOS PRODUTOS {grupo} R${round(total,2)}")




