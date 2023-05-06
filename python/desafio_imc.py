altura = float(input("Insira sua altura em metros: "))
peso = float(input("Insira seu peso em quilogramas: "))

imc = peso / ((altura/100) ** 2)

print("Seu IMC é:", imc)

if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc < 25:
    print("Seu peso está dentro do normal.")
elif imc < 30:
    print("Você está com sobrepeso.")
elif imc < 35:
    print("Você está com obesidade grau 1.")
elif imc < 40:
    print("Você está com obesidade grau 2.")
else:
    print("Você está com obesidade grau 3.")

