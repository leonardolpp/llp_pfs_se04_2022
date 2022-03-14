# Auth: Leonardo Perez
# Version: 0.3.1
# date: 09/03/2022
# dupdateAt: --/--/----

from tkinter import Tk
from tkinter import messagebox
root = Tk()
root.withdraw()

import math


def Exe06():
    print('Ejerc. 6: Declara dos variables e indicar el mayor o igual:')
    M = int(input('Indique un número :  '))
    N = int(input('Indique otro número :  '))
    if M > N:
        print('%d es mayor que %d' % (M, N))
    elif N > M:
        print('%d es mayor que %d' % (N, M))
    else:
        print('%d y %d son iguales...' % (M, N))


def Exe07():
    print('Ejerc. 7: Declara str con tu nombre:')
    NOM = 'Leonardo Pérez'
    print('Bienvenido ', NOM)


def Exe08():
    print('Ejerc. 8: Solicitar str con tu nombre:')
    NOM = input('Indique su Nombre: ')
    print('Bienvenido ', NOM)


def Exe09():
    print('Ejerc. 9: Calcular el área de un círculo:')
    zpi = math.pi
    R = float(input('Inidique el Radio:'))
    CIR = math.pow(R, 2) * zpi
    print('área de un círculo %.3f (%.2f y %.6f)' % (CIR, R, zpi))


def Exe10():
    print('Ejerc. 10: Calcular si un número es par:')
    R = int(input('Inidique un número (entero) : '))
    N = (R % 2)
    if N == 0:
        print('%d es par' % R)
    else:
        print('Impar, para %d, el resto es %d' % (R, N))


def Exe11():
    print('Ejerc. 11: Calcular el precio de un producto con IVA 21%:')
    wIVA = 21.0
    PVP = float(input('Indique el precio: '))
    PVPTOT = PVP * wIVA / 100
    print('Precio total de %.2f es de %.2f (%.1f de IVA)' % (PVP, PVP + PVPTOT, wIVA))


def Exe12():
    print('Ejerc. 12: Muestra los números del 1 al 10 (While):')
    R = 1
    while R <= 10:
        print(R)
        R += 1


def Exe13():
    print('Ejerc. 13: Muestra los números del 1 al 10 (Array):')
    R = 10
    vec = list(range(R + 1))
    del vec[0]
    print(vec)


def Exe14():
    print('Ejerc. 14: Muestra los números del 1 al 100 (divisibles entre 2 y 3):')
    R = 0
    while R <= 100:
        R += 1
        if R == 1:
            print('Inicio:', R)
        elif R % 2 == 0:
            print('Es par:', R)
        elif R % 3 == 0:
            print('Divisible por 3:', R)


def Exe15():
    print('Ejerc. 15: Indicar número de ventas y el importe total')
    V = int(input('Indique el número de Ventas : '))
    if V == 0:
        print('SIN VENTAS')
    else:
        N = 1
        TOTAL = 0.0
        while N <= V:
            P = float(input('Introduzca el importe del producto %d :' % N ))
            if N == 1:
                vec = [P]
            else:
                vec.extend([P])
            TOTAL += P
            N += 1
        print('\Productos comprados:', vec)
        print('Total (%d): %.2f' % (N - 1, TOTAL))


def Exe16():
    print('Ejerc. 16: Indicar día de semana e indicar si es laboral')
    dialaboral = ['LUNES', 'MARTES', 'MIERCOLES', 'MIÉRCOLES', 'JUEVES', 'VIERNES']
    dialibre = ['SABADO','SÁBADO', 'DOMINGO']
    # print('Pendiente: al indicar un dia de semana indicar si es laboral o no.')

    diasem = input('Indique un día de semana : ')

    if diasem.upper() in dialaboral:
        print('Dia laboral (%s)' % diasem)
    elif diasem.upper() in dialibre:
        print('Dia libre (%s)' % diasem)
    else:
        print('El día no existe (%s)' % diasem)


def Exe17():
    print('Ejerc. 17: Tres intentos para password.')
    clave_in = 'ClavePFS'
    intentos = 1
    mensaje = 'Ha consumido los tres intentos...!'
    while intentos <= 3:
        miclave = input('Introduzca el password : ')
        if miclave == clave_in:
            mensaje = 'Enhorabuena..!'
            break
        else:
            print('Password incorrecto (%d).' % intentos)
            intentos += 1
    print(mensaje)


def Exe18():
    print('Ejerc. 18: CalculadoraInversa, dos enteros y su operación atirmética')
    M = int(input('Indique Operando 1º: '))
    N = int(input('Indique Operando 2º: '))
    operac = ('+', '-', '*', '/', '^', '%')
    dicionario = {0: 'La Suma', 1:'La Resta', 2:'El Producto', 3:'La División', 4:'La Potencia',5:'El Resto'}

    # oper = input('Indique operación (' +  str(operac) + ') : ')
    oper = str(input("Indique operación  : "))

    if oper in operac:
        resultado = eval(str(M) + str(oper) + str(N))
        # print('Números %d y %d (%s = %.2f ))' % (M, N, dicionario.get(operac.index(oper)), resultado))
        wmensaje = str(dicionario.get(operac.index(oper))) + ' de ' + str(M) + ' y ' +  str(N) + ' es:\n' + str(resultado)
        messagebox.showinfo(message=wmensaje, title='Resultado')
    else:
        print('#ERROR# Operador incorrecto')
