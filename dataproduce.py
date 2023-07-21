import pandas as pd
import random
from faker import Faker
from random import randrange
from datetime import timedelta

fake = Faker()

# Define produtos e categorias
produtos = {
    "Camisas": 50.0,
    "Blusas": 30.0,
    "Calças": 75.0,
    "Bermudas": 35.0,
    "Acessórios": 20.0,
    "Vestidos": 100.0
}
categorias = ["Masculino", "Feminino", "Infantil"]

# Define funções auxiliares
def gerar_produto(categoria):
    if categoria == "Masculino":
        produtos_disponiveis = {produto: preco for produto, preco in produtos.items() if produto != "Vestidos"}
        return random.choice(list(produtos_disponiveis.items()))
    else:
        return random.choice(list(produtos.items()))

def gerar_tamanho(produto):
    if produto == "Acessórios":
        return None
    else:
        return random.choice(["P", "M", "G"])

def gerar_data_venda(start_date, end_date):
    return start_date + timedelta(days=randrange((end_date - start_date).days))

# Gera DataFrame
def gerar_dados(n):
    start_date = pd.to_datetime('2021-01-01')
    end_date = pd.to_datetime('2023-01-01')
    dados = []
    for _ in range(n):
        data_venda = gerar_data_venda(start_date, end_date)
        categoria = random.choice(categorias)
        produto, preco_base = gerar_produto(categoria)
        tamanho = gerar_tamanho(produto)
        evento_especial = fake.boolean(chance_of_getting_true=20) # 20% de chance de ser True
        promocao = fake.boolean(chance_of_getting_true=30) # 30% de chance de ser True
        if evento_especial:
            preco = round(preco_base * 0.75, 2) # 25% de desconto
        elif promocao:
            preco = round(preco_base * 0.90, 2) # 10% de desconto
        else:
            preco = preco_base
        quantidade = random.randint(1, 140)
        estacao = random.choice(["Primavera", "Verão", "Outono", "Inverno"])
        dados.append([produto, categoria, tamanho, preco, data_venda, quantidade, evento_especial, promocao, estacao])

    df = pd.DataFrame(dados, columns=["Produto", "Categoria", "Tamanho", "Preço", "Data da Venda", "Quantidade", "Evento Especial", "Promoção", "Estação do Ano"])
    return df

# Gera 1000 linhas de dados
df = gerar_dados(250)

# Escreve os dados no Excel
df.to_excel("dados_MAC_Clothes.xlsx", index=False)
