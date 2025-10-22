from  Veiculo import Veiculo
class CaminhaoCarga(Veiculo):
    def __init__(self, marca, modelo, ano_fabricacao, chassi, cor, quilometragem, capacidade_toneladas: float, eixos: int):
        super().__init__ (marca, modelo, ano_fabricacao, chassi, cor, quilometragem)
        self.capacidade_toneladas = capacidade_toneladas
        self.eixos = eixos
        self.vistorias = []

    def registrar_vistoria(self, motivo:str , multa: float = 0):
        self.vistorias.append((motivo,multa))
        print(f'Motivo da vistoria: {motivo}\nValor da multa: {multa}')

    def exibir_informacoes(self, detalhado: bool):
        super().exibir_informacoes(detalhado)
        print(f'Capacidade em toneladas: {self.capacidade_toneladas}\nEixos: {self.eixos}')