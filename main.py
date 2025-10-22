from CarroPasseio import CarroPasseio
from CaminhaoCarga import CaminhaoCarga

veiculo001 = CarroPasseio ('Toyota', 'Corolla' , 2018 , '9BWL232A2XJ078912' , 'preto' , 20000 , 2 , 'Gasolina')
veiculo002 = CarroPasseio ('Ford' , 'Mustang' , 2020 , '1FA6P8TH0L5101234', 'cinza' , 10000 , 4 , 'Elétrico')
veiculo003 = CaminhaoCarga('Volvo' , 'FH16', 2015 , 'VOL123456789' , 'Branco' , 120000 , 20 , 4)
                         
veiculo001.exibir_informacoes(True)
veiculo001.calcular_depreciacao(0.03)
print('\n')
veiculo002.exibir_informacoes(False)
veiculo002.calcular_depreciacao(0.04)
print('\n')
veiculo003.exibir_informacoes(True)
veiculo003.registrar_vistoria('Excesso de peso', 1500.00)
veiculo003.registrar_vistoria('Farol queimado', 200.00)
veiculo003.registrar_vistoria('Documentação em dia')  # sem multa
print("\nLista de vistorias registradas:")
print(veiculo003.vistorias)
print('\n')