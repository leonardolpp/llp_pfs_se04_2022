# Auth: Leonardo Perez
# Version: 0.0.1
# date: 09/03/2022
# dupdateAt: --/--/----

from tkinter import Tk
from tkinter import messagebox
root = Tk()
root.withdraw()

import math


def Exe06():
    M = int(input('Indique un número: '))
    N = int(input('Indique otro número: '))
    if M > N:
        print('%d es mayor que %d' % (M, N))
    elif N < M:
        print('%d es mayor que %d' % (N, M))
    else:
        print('%d y %d son iguale' % (M, N))


def Exe07():
    NOM = 'Leonardo Pérez'
    print('Bienvenido ', NOM)


def Exe08():
    NOM = int(input('Indique su Nombre: '))
    print('Bienvenido ', NOM)


def Exe09():
    R = float(input('Inidique el Radio:'))
    CIR = math.pow(R, 2) * zpi
    print('área de un círculo %.3f ' % CIR)


def Exe10():
    R = int(input('Inidique un número:'))
    N = (R % 2)
    if N == 0:
        print('%d es par' % R)
    else:
        print('Impar, para %d, el resto es %d' % (R, N))


def Exe11():
    wIVA = 21.0
    PVP = float(input('Indique el precio: '))
    PVPTOT = PVP * wIVA / 100
    print('Precio total de %.2f es de %.2f (%.2f de IVA)' % (PVP, PVP + PVPTOT, wIVA))


def Exe12():
    R = 0
    while R <= 10:
        R += 1
        print(R)


def Exe13():
    R = 10
    vec = list(range(R + 1))
    del vec[0]
    print(vec)


def Exe14():
    R = 0
    while R <= 100:
        R += 1
        if R % 2 == 0:
            print('Es par:', R)
        elif R % 3 == 0:
            print('Divisible por 3:', R)


def Exe15():
    V = int(input('Cuantas ventas?:'))
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


def Exec16():
    print('Pendiente: al indicar un dia de semana indicar si es laboral o no.')


def Exec18():
    # print('Pendiente: dos operandos y luego indicar la operacion')
    M = int(input('Indique Operando 1º: '))
    N = int(input('Indique Operando 2º: '))
    # print('\t + suma los dos operandos')
    # print('\t - resta los operandos')
    # print('\t * multiplica los operandos')
    # print('\t / divide, resultado float')
    # print('\t ^ 1º oper base y 2º exponente')
    # print('\t % módulo, resto entre 1º y 2º')
    operac =['+', '-', '*', '/', '^','%']
    dicionario = {0: 'La Suma', 1:'La Resta', 2:'El Producto', 3:'La División', 4:'La Potencia',5:'El Resto'}
    oper = input('Indique operación (' +  str(operac) + '):')

    if oper in operac:
        resultado = eval(str(M) + str(oper) + str(N))
        wmensaje = str(dicionario.get(operac.index(oper))) + ' de ' + str(M) + ' y ' +  str(N) + ' es:\n' + str(resultado)
        # print('Números %d, %d (%s) = %.2f ))' % (M, N, dicionario.get(operac.index(oper)), resultado))
        messagebox.showinfo(message=wmensaje, title='Resultado')
    else:
        print('#ERROR# Operador incorrecto')
