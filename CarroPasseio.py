from  Veiculo import Veiculo
class CarroPasseio(Veiculo):
    def __init__(self, marca, modelo, ano_fabricacao, chassi, cor, quilometragem, numero_portas, tipo_combustivel):
        super().__init__ (marca, modelo, ano_fabricacao, chassi, cor, quilometragem)
        self.numero_portas = numero_portas
        self.tipo_combustivel = tipo_combustivel
