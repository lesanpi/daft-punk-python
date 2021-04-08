from __future__ import print_function, unicode_literals
from discografia_daft_punk import *
# Para intalar las librerias de colores y titulos cools
import subprocess
import sys


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


# Instalacion
install("clint")  # Colores
install("PyInquirer")  # Preguntas
install("pyfiglet==0.7")  # Titulos cool

from pyfiglet import Figlet
from PyInquirer import prompt, print_json, style_from_dict, Token, Separator
from clint.textui import colored, puts
from os import system, name

# Limpiar la pantalla
def clear():
    # Windows
    if name == 'nt':
        _ = system('cls')
    # Mac and Linux
    else:
        _ = system('clear')

# Styles
style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: 'bold #673ab7',
})

# Titulo
title = Figlet(font='slant')
main_menu_actions = [
    "Disco con mayor cantidad ventas?",
    "Disco con menor cantidad ventas?",
    "Disco con mayor duracion?",
    "Disco con mas canciones?",
    "Listar orden cronologico?",
    "Disco mejor posicionado en las listas de Estados Unidos?",
    "Cuantos discos sacaron por cada discografia?",
    "Cual fue el disco con mayor cantidad de certificaciones?"
]
# Menu
main_menu = [
    {
        "type": "list",
        "message": "Menu",
        "name": "action",
        "choices": main_menu_actions + [Separator(), "Cerrar"]
    }
]

def mayor_estadistica(estadistica):
    disco_mayor_estadistica = list(discografia.keys())[0]
    for disco in discografia:
        if estadistica == 'certificaciones':
            cant_certificaciones_disco = sum(discografia[disco][estadistica].values())
            cant_certificaciones_disco_mayor = sum(discografia[disco_mayor_estadistica][estadistica].values())

            if cant_certificaciones_disco > cant_certificaciones_disco_mayor:
                disco_mayor_estadistica = disco

        elif estadistica in ['Diamante', 'Platino', 'Oro']:
            cant_certificaciones_disco = discografia[disco]['certificaciones'][estadistica]
            cant_certificaciones_disco_mayor = discografia[disco_mayor_estadistica]['certificaciones'][estadistica]
            if cant_certificaciones_disco > cant_certificaciones_disco_mayor:
                disco_mayor_estadistica = disco

        else:
            if discografia[disco][estadistica] > discografia[disco_mayor_estadistica][estadistica]:
                disco_mayor_estadistica = disco

    return disco_mayor_estadistica


def menor_estadistica(estadistica):
    disco_menor_estadistica = list(discografia.keys())[0]
    for disco in discografia:
        if discografia[disco][estadistica] < discografia[disco_menor_estadistica][estadistica]:
            disco_menor_estadistica = disco

    return disco_menor_estadistica


def ordenar_cronologicamente():
    lista_discos = [disco for disco in discografia]
    lista_ordenada = [disco for disco in discografia]
    for ix1, disco_1 in enumerate(lista_discos):
        #print("*", disco_1, discografia[disco_1][estadistica])
        for ix2, disco_2 in enumerate(lista_discos):

            if discografia[disco_1]['fecha_publicación'] > discografia[disco_2]['fecha_publicación'] and ix2 > ix1:
                #print("-", disco_2, discografia[disco_2][estadistica])
                #print(disco_2, "mayor que", disco_1)
                # Intercambio
                lista_ordenada[ix1], lista_ordenada[ix2] = lista_ordenada[ix2], lista_ordenada[ix1]

    return lista_ordenada


def discos_por_discografia():
    discos_por_discografia = {}

    for disco in discografia:
        if discografia[disco]['discografía'] in list(discos_por_discografia.keys()):
            discos_por_discografia[discografia[disco]['discografía']] += 1
        else:
            discos_por_discografia[discografia[disco]['discografía']] = 1

    return discos_por_discografia


def main():
    clear()
    print(title.renderText("Daft Punk"))
    while True:
        main_menu_action = prompt(main_menu, style=style)

        # Cerrar programa
        if main_menu_action['action'] == 'Cerrar':
            break

        elif main_menu_action['action'] == main_menu_actions[0]:
            print(colored.yellow("1. El disco mas vendido:"), mayor_estadistica('total_ventas'))

        elif main_menu_action['action'] == main_menu_actions[1]:
            print(colored.yellow("2. El disco menos vendido:"), menor_estadistica('total_ventas'))

        elif main_menu_action['action'] == main_menu_actions[2]:
            print(colored.yellow("3. El disco de mayor duracion:"), mayor_estadistica('duracion_segundos'))

        elif main_menu_action['action'] == main_menu_actions[3]:
            print(colored.yellow("4. El disco con mas canciones:"), mayor_estadistica('total_canciones'))

        elif main_menu_action['action'] == main_menu_actions[4]:
            print(colored.yellow("5. Orden cronologico:"))
            cronologia = ordenar_cronologicamente()
            for disco in cronologia:
                print(disco, discografia[disco]['fecha_publicación'])

        elif main_menu_action['action'] == main_menu_actions[5]:
            print(colored.yellow("6. El disco con mejor posicionado en las listas de Estados Unidos"),
                  menor_estadistica('posicionamiento_en_usa'))

        elif main_menu_action['action'] == main_menu_actions[6]:
            print(colored.yellow("7. Discos por discografia:"))
            discografia_discos = discos_por_discografia()
            for discografia_ in discografia_discos:
                print(discografia_, ":",discografia_discos[discografia_], "Disco/s")

        elif main_menu_action['action'] == main_menu_actions[7]:
            print(colored.yellow("8. El disco con mayor certificaciones:"), mayor_estadistica("certificaciones"))

        elif main_menu_action['action'] == main_menu_actions[8]:
            print(colored.yellow("9. El disco con mayor certificaciones diamante:"), mayor_estadistica("Diamante"))

        elif main_menu_action['action'] == main_menu_actions[9]:
            print(colored.yellow("10. El disco con mayor certificaciones platino:"), mayor_estadistica("Platino"))

        elif main_menu_action['action'] == main_menu_actions[10]:
            print(colored.yellow("11. El disco con mayor certificaciones oro:"), mayor_estadistica("Oro"))


if __name__ == '__main__':
    main()
