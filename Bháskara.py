#Criar calculadora de equação do segundo grau
#definir função para tirar raiz quadrada
def square(x):
    x = x ** (1/2)
    return x
#Apresentação
print("_____________________________________")
print("")
print("Olá, vamos resolver essa equação? ")
print("___________________________________")
#Pegar os termos fundamentais
a = int(input("Quem é 'a'? "))
b = int(input("Quem é 'b'? "))
c = int(input("Quem é 'c'? "))
print(f"Sua equação é {a}x²+({b}x)+({c})= 0")
delta = b*b - 4*a*c
print(f"Δ = {delta}")
#Tirar as raízes
x1 = (-b + square(delta))/(2*a)
x2 = (-b - square(delta))/(2*a)
#Definir a solução final da equação
if delta < 0:
    print("Não há raízes reais para essa equação!")
else:
    if delta == 0:
        print(f"As duas raízes são iguais a {x1}")
    else:
        print(f"As duas raízes reais são iguais a {x1} e {x2}")

        