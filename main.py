from zoo import Zoo
#from animal import Animal
from leon import Leon
from jirafa import Jirafa
from hipopotamo import Hipopotamo
from pinguino import Pinguino

import os

def menu(): 
    opcion = -1
    while opcion < 0 or opcion > 5:
        os.system("cls")
        print(f'Menú: {zoo1.nombre}')
        print("[1] Agregar animal")
        print("[2] Eliminar animal")
        print("[3] Desplegar información de los animales")
        print("[4] Mostrar los herbívoros")
        print("[5] Mostrar los carnívoros")
        print("[0] Salir")
        try:
            opcion = int(input("Ingrese su opción: "))
        except:
            input("El valor ingresado no parece ser un número...")
        if opcion < 0 or opcion > 5:
            input("Opción ingresada no válida, presione ENTER para continuar...")
    return opcion

zoo1 = Zoo('0071 Zoo')
opcion = 1
while opcion > 0:
    opcion = menu()
    if opcion == 1:
        print('Ingreso opción de nuevo animal')
        animal_type = -1
        while animal_type < 0 or animal_type > 4:
            print('Ingrese\n [1]para agregar león\n [2]para agregar jirafa\n [3]para agregar hipopotamo\n [4]para agregar pinguino\n')
            try:
                animal_type = int(input("Ingrese su opción: "))
            except:
                input("El valor ingresado no parece ser un número...")
            if animal_type < 0 or animal_type > 4:
                input("Opción ingresada no válida, presione cualquier tecla para continuar...")


        nombre = input('Ingrese nombre: ').upper()
        edad = int(input('Ingrese edad del animal:'))
        nivel_salud = int(input('Ingrese nivel de salud:'))
        nivel_felicidad = int(input('Ingrese nivel de felicidad:'))
        if animal_type == 1:
            melena = input('Tiene melena? [Si/No]:')
            if melena.upper() == 'SI':
                melena = True
            else:
                melena = False
            nuevo_animal = Leon(nombre, edad, nivel_salud, nivel_felicidad, melena)
        elif animal_type == 2:
            nuevo_animal = Jirafa(nombre, edad, nivel_salud, nivel_felicidad)
        elif animal_type == 3:
            nuevo_animal = Hipopotamo(nombre, edad, nivel_salud, nivel_felicidad)
        elif animal_type == 4:
            nuevo_animal = Pinguino(nombre, edad, nivel_salud, nivel_felicidad)    
        if zoo1.agregar_animal(nuevo_animal) == True:
            print("Felicitaciones, animal ingresado satisfactoriamente...")
        else:
            print("Lamentamos informar que el animal ya existe en nuestros registros...")
        input('Presione una tecla para continuar...')        
    elif opcion == 2:
        nombre = input('Ingrese nombre de animal a remover: ').upper()
        if zoo1.eliminar_animal(nombre) == True:   
             print("Se ha removido satisfactoriamente...")
        else:
            print("Lamentamos informar que el animal no existe en nuestros registros...")
        input('Presione una tecla para continuar...')           
    elif opcion == 3:
        zoo1.print_all_info()
        input('Presione una tecla pra continuar...')
    elif opcion == 4:
        zoo1.print_herbivoros()
        input('Presione una tecla para continuar...')
    elif opcion == 5:
        zoo1.print_carnivoros()
        input('Presione una tecla pra continuar...')