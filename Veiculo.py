class Veiculo:
    def __init__(self, marca: str, modelo: str, ano_fabricacao: int, chassi: str, cor: str, quilometragem: float):
        self.marca = marca
        self.modelo = modelo
        self.ano_fabricacao = ano_fabricacao
        self.chassi = chassi
        self.cor = cor
        self.quilometragem = quilometragem
        
    def registrar_manutencao(self, tipo: str, custo: int):
        print(f'O veículo do tipo {tipo} tem o custo de R$ {custo}')

    def exibir_informacoes(self, detalhado: bool):
       print(f'\nMarca: {self.marca}\nModelo: {self.modelo}\nQuilometragem: {self.quilometragem}')
       if detalhado:
            print(f'Chassi: {self.chassi}\nCor: {self.cor}\nAno de Fabricação: {self.ano_fabricacao}')