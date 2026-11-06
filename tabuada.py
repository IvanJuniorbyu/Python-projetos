# Função reutilizável - limite é opcional, padrão 10
def mostrar_tabuada(numero, limite=10):
    print(f'\n--- Tabuada do {numero} até {limite} ---')
    for i in range(1, limite + 1):
        resultado = i * numero
        print(f'{i:2} x {numero:2} = {resultado:3}')  # :2 e :3 alinham a saída
    print("-" * 30)

# Proteção contra crash se digitar letra
while True:
    try:
        numero = int(input('Escolha um número para a tabuada: '))
        break
    except ValueError:
        print("❌ Valor inválido! Digite apenas números inteiros.\n")

# Usuário escolhe o limite ou usa padrão 10
limite_input = input('Até quanto vai? [Enter = 10]: ')
if limite_input == "":
    limite = 10
else:
    try:
        limite = int(limite_input)
    except ValueError:
        print("Valor inválido, usando 10 como padrão.")
        limite = 10

mostrar_tabuada(numero, limite)