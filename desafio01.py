nome = input('Digite seu nome: ')
print(f'Bem-vindo {nome}!')


dia = input('Digite o dia que você nasceu: ')
mes =input('Digite o mes que você nasceu: ')
ano = input('Digite o ano que você nasceu: ')
print (f'{dia}/{mes}/{ano}')

numero1= int(input('digite um número: '))
numero2= int(input('digite outro número: '))
resultado = numero1 + numero2

print(f'o resultado da soma dos números que você escolheu é {resultado}')


raio = int(input('Digite o raio da circunferência: '))
pi = 3.141592
formula = pi * (raio**2)
print(f'A área da circunferência é: {formula}')

fah = int(input("digite a temperatura em fahrenheit: "))
formula2 = (fah - 32) * (5/9)
print(f'essa temperatura, em graus celcius, é: {formula2}')