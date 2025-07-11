def GetNumberValue(texto):
    correctValue = False
    while not correctValue:
        try:
            number = int(input(texto))
        except:
            print("Error:Se tiene que introducir un numero")
        else:
            correctValue = True
    return number
def Sum():
    print("---Suma---")
    v1 = GetNumberValue("Introduce primer valor:")
    v2 = GetNumberValue("Introduce el segundo valor:")
    print("El resultado de la suma es:", v1 + v2)
def Subtract():
    print("---Resta---")
    v1 = GetNumberValue("Introduce primer valor:")
    v2 = GetNumberValue("Introduce el segundo valor:")
    print("El resultado de la resta es:", v1 - v2)
def Multiply():
    print("---Multiplicacion---")
    v1 = GetNumberValue("Introduce primer valor:")
    v2 = GetNumberValue("Introduce el segundo valor:")
    print("El resultado de la multiplicacion es:", v1 * v2)
def Divide():
    print("---Divicion---")
    v1 = GetNumberValue("Introduce primer valor:")
    v2 = GetNumberValue("Introduce el segundo valor:")
    if v2 == 0:
        print("Error: Se intento dividir entre 0")
    else:
        print("El valor de la division es:", v1 / v2)


        
def Menu():
    print("""---Calculadora Python---
1.Sumar
2.Restar
3.Multiplicar
4.Dividir
5.Salir
""")
    
programIsRunning = True

while programIsRunning:
    Menu()
    opc = GetNumberValue("Elige una opcion:")
    if opc == 1:
        Sum()
    elif opc == 2:
        Subtract()
    elif opc == 3:
        Multiply()
    elif opc == 4:
        Divide()
    elif opc not in [1,2,3,4,5]:
        print("Opcion no valida!")
    else:
        print("Se cierra el programa.")
        programIsRunning = False
