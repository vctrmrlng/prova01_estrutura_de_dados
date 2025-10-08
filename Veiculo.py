class Veiculo:
    def __init__(self, marca, modelo, ano_fabricacao, chassi, cor, quilometragem):
        self.marca = marca
        self.modelo = modelo
        self.ano_fabricacao = ano_fabricacao
        self.chassi = chassi
        self.cor = cor
        self.quilometragem = quilometragem
        
def registrar_manutencao(tipo, custo):
    print(f'O veículo do tipo {tipo} tem o custo de R$ {custo}')

def exibir_informações(detalhado):
    print(f'''  Marca: {self.marca}
                    Modelo: {self.modelo} 
                    Quilometragem: {self.quilometragem}
              ''')
    if not detalhado:
        break
    else print(f'''Chassi: {self.chassi}
                   Cor: {self.cor}
                   Ano de Fabricação: {self.ano}
                ''')