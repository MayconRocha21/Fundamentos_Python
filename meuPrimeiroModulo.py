#Criando um dicioário com preços de manutenção
precos_manutencao = {
    "Troca de Óleo": 50,
    "Filtro de Ar": 20,
    "Pastilhas de Freio": 80,
    "Bateria": 100,
    "Alinhamento": 60
}

#Criando um dicioário com tempos de manutenção
tempo_manutencao = {
    "Troca de Óleo": 30,
    "Filtro de Ar": 15,
    "Pastilhas de Freio": 45,
    "Bateria": 60,
    "Alinhamento": 40
}


#Função para calcular o Custo de manutenção dos itens do pedido
def calcular_preco_pedido_manutencao(pedido_servico):
    
    preco_total = 0

    for item, preco in precos_manutencao.items():
        if item in pedido_servico:
            preco_total += preco
    
    return preco_total


#Função para calcular o tempo de manutenção dos itens do pedido
def calcular_tempo_pedido_manutencao(pedido_servico):
    tempo_total = 0
    for item, tempo in tempo_manutencao.items():
        if item in pedido_servico:
            tempo_total += tempo
    return tempo_total


# Função principal para fazer o pedido de manutenção
def fazer_pedido_manutencao(pedido_servico):

    custo_total = calcular_preco_pedido_manutencao(pedido_servico)
    tempo_total = calcular_tempo_pedido_manutencao(pedido_servico)

    print("SERVICE_CAR AUTO CENTER")
    print("------------------------------------")
    print("Itens de manutenção:")
    for item in pedido_servico:
        print(f"{item} = R${precos_manutencao[item]} +- {tempo_manutencao[item]} min.")

    print("------------------------------------")
    print(f"Valor total = R$ {custo_total}")
    print(f"Tempo total = {tempo_total} minutos")
    