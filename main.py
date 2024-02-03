peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc =peso /(altura * altura)

print("Seu IMC é: " , imc)

if imc < 16:
    print("Peso Deficitário Grave")

elif imc < 18.5:
    print("Abaixo do Peso")    

elif imc < 24.9:
    print("Peso Normal")

elif imc < 29.9:
    print("Acima do Peso")

elif imc < 34.9:
    print("Obesidade Grau 1")

elif imc < 34.9:
    print("Obesidade Grau 1")

elif imc < 40:
    print("Obesidade Grau 2")

else:
    print("Obesidade Grau 3")
 

