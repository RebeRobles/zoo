from leon import Leon
from jirafa import Jirafa
from hipopotamo import Hipopotamo
from pinguino import Pinguino

class Zoo:

    def __init__(self, nombre, lista_animales = []):
        self.nombre = nombre
        self.lista_animales = lista_animales

    def agregar_animal(self, nuevo_animal):
            for animal in self.lista_animales:
                if animal.nombre == nuevo_animal.nombre:
                    return False
            self.lista_animales.append(nuevo_animal)
            return True

    def eliminar_animal(self, nombre):
        for animal in self.lista_animales:
            if animal.nombre == nombre:
                self.lista_animales.remove(animal)
                return True
        return False

    def print_all_info(self):
        print("-"*30, self.nombre, "-"*30)
        for animal in self.lista_animales:
            print(animal.display_info())    

    def listar_herbivoros(self):
        herbivoros = []
        for animal in self.lista_animales:
            if isinstance(animal,Jirafa) or isinstance(animal,Hipopotamo):
                herbivoros.append(animal)
        return herbivoros

    def listar_carnivoros(self):
        carnivoros = []
        for animal in self.lista_animales:
            if isinstance(animal,Leon) or isinstance(animal,Pinguino):
                carnivoros.append(animal)
        return carnivoros

    def print_herbivoros(self):
        print('-'*30, self.nombre, 'Lista de Herbívoros', '-'*30)
        for animal in self.listar_herbivoros():
            print(animal.display_info())

    def print_carnivoros(self):
        print('-'*30, self.nombre, 'Lista de Carnívoros', '-'*30)
        for animal in self.listar_carnivoros():
            print(animal.display_info())        