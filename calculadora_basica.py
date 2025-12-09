print("==Calculadora Básica==")

num1 = float(input("Ingresa el primer numero: "))
operacion = input("Elige una operacion (+, -, *, /): ")
num2 = float(input("Ingresa el segundo numero: "))

if operacion == "+":
    resultado = num1 + num2
elif operacion == "-":
    resultado = num1 - num2
elif operacion == "*":
    resultado = num1 * num2
elif operacion == "/":
    resultado = num1 / num2
else:
    print("Operacion no valida")
    exit()

print("Resultado:", resultado)
