from  Veiculo import Veiculo
class CaminhaoCarga(Veiculo):
    def __init__(self, marca, modelo, ano_fabricacao, chassi, cor, quilometragem, capacidade_toneladas, eixos):
        super().__init__ (marca, modelo, ano_fabricacao, chassi, cor, quilometragem)
        self.capacidade_toneladas = capacidade_toneladas
        self.eixos = eixos