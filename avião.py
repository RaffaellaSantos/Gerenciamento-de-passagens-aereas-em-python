#80 lugares ao total, dedicados aos passageiros; A e B 20 lugares; C e D 20 lugares
#A passagem custa 1500 reais;

fileira_A = []
fileira_B = []
fileira_C = []
fileira_D = []
faturamento = []
preco_passagem = 1500

#Funções para marcar assento
def comprar_passagem(passagens):
  print(f'Fileiras A, B, C e D de 1 a 20')
  for k in range(passagens):
    x = 0
    while x == 0:
      print(f'Passagem número {k + 1}')
      lugar = input('Escolha sua fileira(A,B,C,D):\n').upper()
      if lugar in ['A', 'B','C', 'D']:
        assento_list = fileira_A if lugar == 'A' else fileira_B if lugar == 'B' else fileira_C if lugar == 'C' else fileira_D
        if reservar_lugar(lugar,assento_list):
          x += 1
      else:
        print('Essa fileira é inválida!')

def reservar_lugar(fileira,assento_list):
  assento = escolher_assento(fileira)
  if assento not in assento_list:
    assento_list.append(assento)
    print('assento reservado')
    return True
  else:
    print('assento ocupado')
    return False

def escolher_assento(fileira):
  while True:
    assento = input(f'Escolha seu assento na fileira {fileira} (de 1 a 20)\n')
    try:
      assento = int(assento)
      if 1 <= assento <= 20:
        return assento
      else:
        print('Assento Inválido')
    except:
      print('Esse caractere não é válido')

#Função para o desconto da idade
def idade_passageiro(idade,preco_passagem):
  if idade < 5 or idade > 65:
    preco_passagem = preco_passagem *0.5
    faturamento.append(preco_passagem)
  else:
    faturamento.append(preco_passagem)

#Verificar se o voo está autorizado
def voo_autorizado():
    faturamento_total = sum(faturamento)
    taxa_ocupacao = len(faturamento)*100 / 80
    if len(faturamento) < 35:
      print('Sua viagem foi cancelada. O vôo não alcançou a capacidade suficiente.')
      print(f'O montante total a ser devolvido da viagem cancelada é de: R${faturamento_total:.2f}\nE a taxa de ocupação de passageiros é de: {taxa_ocupacao:.2f}%')
      print('Consulte a agência para remarcar seu vôo, agradecemos a preferência.')
    else:
      print(f'O faturamento total da viagem é de: R${faturamento_total:.2f}\nE a taxa de ocupação de passageiros é de: {taxa_ocupacao:.2f}%')
      print('Boa Viagem!')

y = 0
while y == 0:
    passagens = input('Quantas passagens você deseja comprar?(Para encerrar digite -1)\n')
    try:
      passagens = int(passagens)
      if passagens == -1:
        y += 1
      else:
        for i in range(passagens):
          idade = int(input(f'Idade do passageiro {i + 1}:\n'))
          idade_passageiro(idade,preco_passagem)
        comprar_passagem(passagens)
    except:
      print('Você digitou algo errado')
voo_autorizado()