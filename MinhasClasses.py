class Carro:

    def __init__(self, modelo, marca, cor, ano):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.ano = ano
        self.ligado = False

    def set_modelo(self, novo_modelo):
        self.modelo = novo_modelo

    def get_modelo(self):
        return self.modelo

    def set_ano(self, novo_ano):
        self.ano = novo_ano

    def get_ano(self):
        return self.ano

    def get_info_carro(self):
        return self.ligado

    def set_ligado(self, status):
        self.ligado = status


