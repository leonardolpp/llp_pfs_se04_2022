# Auth: Leonardo Perez
# Version: 0.1.1
# date: 11/03/2022
# dupdateAt: --/--/----

# solicitar la ejecucion de los ejercicios

from se04_ex.ejercicios import *


def menuejercicios():
    vexecs = (0, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 99)

    ejercicio = int(input('Indique el ejercico (6 al 18) : '))

    if ejercicio in vexecs:
        print('+ - - - - - - - - - - - - - - - - - - +')
        if ejercicio == 0:
            print('No se ejecutará ningún ejercio')
        elif ejercicio == 6:
            Exe06()
        elif ejercicio == 7:
            Exe07()
        elif ejercicio == 8:
            Exe08()
        elif ejercicio == 9:
            Exe09()
        elif ejercicio == 10:
            Exe10()
        elif ejercicio == 11:
            Exe11()
        elif ejercicio == 12:
            Exe12()
        elif ejercicio == 13:
            Exe13()
        elif ejercicio == 14:
            Exe14()
        elif ejercicio == 15:
            Exe15()
        elif ejercicio == 16:
            Exe16()
        elif ejercicio == 17:
            Exe17()
        elif ejercicio == 18:
            Exe18()
        elif ejercicio == 99:
            Exe06()
            Exe07()
            Exe08()
            Exe09()
            Exe10()
            Exe11()
            Exe12()
            Exe13()
            Exe14()
            Exe15()
            Exe16()
            Exe17()
            Exe18()
    else:
        print('Ejercicio NO contemplado: %d' % ejercicio)
