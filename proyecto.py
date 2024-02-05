"""
 Crear un administrador de recetas, leer, crear, eliminar

 1- el programaa debe dar la bienvenida
 2- ruta donde estan las recetas
 3- cantidad de recetas
 4- menúcon las opciones de: leer, crear receta, crear categoria, eliminar receta, eliminar categoria,
 finalizar programa
 op 1 - elegir categoria, mostrar recetas, elegir receta, leer receta
 2 - elegir categoria, crear nombre, crear contenido
 3- nombre categoria, crear carpeta
 4 - lo mismo que la op 1 pero este elimina
 5 - elegir categoria, eliminar
 6 - salirse

 op a tener en cuenta
 tener todoo en while op != 6
 usar system('cls')
 buscar documentación de Path
 crear funciones (todas las que crea que necesite)
 crear flujo del programa

"""

from pathlib import Path
import os
from os import system

recetas = Path('C:/Users/Usuario/Desktop/python/dia 6')


def cantidad_recetas(ruta):
    contador = 0
    for li in Path(ruta).glob('**/*.txt'):
        if li:
            contador += 1
    print(f'hay {contador} recetas')


def elegir_catg():
    inicio = Path.home()
    ruta = Path(inicio, 'Desktop', 'python', 'dia 6', 'Recetas')

    print(os.listdir(f'{ruta}'))

    ctg = input('Qué categoria vas a escoger?: ')

    categ = ruta / f'{ctg}'

    system('cls')

    """categoria = open(categ)
    print(categoria.read())"""

    contador = 0
    # Mostrar que hay en la carpeta
    for li in Path(categ).glob('*.txt'):
        # Mostrar Txt
        # print(l.stem)
        # Leer txt
        # print(l.read_text())
        if li:
            contador += 1
    print(f'en esta categoria hay {contador} recetas')
    op = input('quieres saber cuales son?:')
    # Limpiar
    system('cls')
    if op == 'si' or op == 's' or op == 'Si' or op == 'SI':
        for li in Path(categ).glob('*.txt'):
            # Mostrar Txt
            print(li.stem)

        op2 = input('Quieres leer una receta?: ')
        if op2 == 'si' or op2 == 's' or op2 == 'Si' or op2 == 'SI':

            rect = input('Cual?: ')
            # Leer receta
            leer = categ / f'{rect}.txt'
            mi_receta = open(leer)
            print(mi_receta.read())

            main()
            # Limpiar
            system('cls')
    else:
        main()
        # Leer txt
        # print(l.read_text())


def crear_rect():
    inicio = Path.home()
    ruta = Path(inicio, 'Desktop', 'python', 'dia 6', 'Recetas')

    print(os.listdir(f'{ruta}'))

    ctg = input('Qué categoria vas a escoger?: ')

    system('cls')

    categ = ruta / f'{ctg}'

    nombre = input(f'Qué nombre le pondrás a tu receta de {ctg}?: ')

    rta_nombr = os.path.join(f'{categ}', f'{nombre}.txt')
    tdo = open(rta_nombr, "a")

    system('cls')

    escribir = input('Ahora escribe tu receta: ')
    tdo.write(f'{escribir}')
    tdo.close()

    # Return menú principal
    main()

    system('cls')


def crear_ctg():

    inicio = Path.home()
    ruta = Path(inicio, 'Desktop', 'python', 'dia 6', 'Recetas')


# Traer todas las carpetas de una ruta especifica
    print(os.listdir(f'{ruta}'))

    cat_nw = input('¿ Cual es el nombre de la categoria a crear: ?')

    system('cls')

    ctg_join = os.path.join(f'{ruta}', f'{cat_nw}')

    os.makedirs(ctg_join)

    print('Categoria creada...')
    main()

    system('cls')


def delete_rec():
    inicio = Path.home()
    ruta = Path(inicio, 'Desktop', 'python', 'dia 6', 'Recetas')

    # Traer todas las carpetas de una ruta especifica
    print(os.listdir(f'{ruta}'))

    ctg = input('Qué categoria vas a escoger?: ')
    inicio = Path.home()
    ruta = Path(inicio, 'Desktop', 'python', 'dia 6', 'Recetas')
    categ = ruta / f'{ctg}'

    system('cls')

    contador = 0
    # Mostrar que hay en la carpeta
    for li in Path(categ).glob('*.txt'):
        # Mostrar Txt
        # print(l.stem)
        # Leer txt
        # print(l.read_text())
        if li:
            contador += 1
    print(f'en esta categoria hay {contador} recetas')
    op = input('quieres saber cuales son?:')
    # Limpiar
    system('cls')
    if op == 'si' or op == 's' or op == 'Si' or op == 'SI':
        for li in Path(categ).glob('*.txt'):
            # Mostrar Txt
            print(li.stem)
        op2 = input('Cual receta vas a eliminar?: ')
        # eliminar receta
        rt_receta = os.path.join(f'{categ}', f'{op2}.txt')
        os.remove(rt_receta)
        print('Receta eliminada...')

        main()

        system('cls')
    else:
        main()
        # Leer txt
        # print(l.read_text())


def delete_catg():
    inicio = Path.home()
    ruta = Path(inicio, 'Desktop', 'python', 'dia 6', 'Recetas')

    # Traer todas las carpetas de una ruta especifica
    print(os.listdir(f'{ruta}'))

    cat_nw = input('¿ Cual es el nombre de la categoria a eliminar?: ')

    ctg_join = os.path.join(f'{ruta}', f'{cat_nw}')

    os.rmdir(ctg_join)

    print('Categoria eliminada...')
    system('cls')
    main()


def main():
    print('')
    nombre = input('Dame tu nombre: ')
    system('cls')
    rsp = ''

    print('1. Crear categorias')
    print('2. Crear recetas')
    print('3. Leer recetas')
    print('4. Eliminar recetas')
    print('5. Eliminar categorias')
    print('6. Salir')

    while rsp not in ['1', '2', '3', '4', '5', '6']:
        print('')
        rsp = input(f'Hola {nombre}, ¿Qué deseas hacer?: ')

    if rsp == '1':
        crear_ctg()
    elif rsp == '2':
        crear_rect()
    elif rsp == '3':
        elegir_catg()
    elif rsp == '4':
        delete_rec()
    elif rsp == '5':
        delete_catg()
    elif rsp == '6':
        print('Saliendo...')
        exit()


main()

# Hecho 02/02/2024
# elegir_catg()

# Hecho  03/02/2024
# crear_rect()

# Hecho 03/02/2024
# crear_ctg()

# Hecho 03/02/2024
# delete_rec()

# Hecho 03/02/2024
# delete_catg()
