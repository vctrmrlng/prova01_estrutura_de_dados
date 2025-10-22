from  Veiculo import Veiculo
from datetime import date

class CarroPasseio(Veiculo):
    def __init__(self, marca, modelo, ano_fabricacao, chassi, cor, quilometragem, numero_portas: int, tipo_combustivel: str):
        super().__init__(marca, modelo, ano_fabricacao, chassi, cor, quilometragem)
        self.numero_portas = numero_portas
        self.tipo_combustivel = tipo_combustivel

    # def calcular_depreciacao (self, anos_uso: int, taxa_extra: float):
    #     print(f"A taxa de depreciação é de: {anos_uso*taxa_extra}")
    #     return anos_uso*taxa_extra
    
    def calcular_depreciacao (self, taxa_extra: float):
        ano_atual = date.today().year
        anos_uso = ano_atual - self.ano_fabricacao
        taxa = anos_uso*taxa_extra
        print(f"A taxa de depreciação é de: {taxa:.2f}")
        return taxa


    def exibir_informacoes(self, detalhado: bool):
        super().exibir_informacoes(detalhado)
        print(f'N° de portas: {self.numero_portas}\nTipo de combustível: {self.tipo_combustivel}' )