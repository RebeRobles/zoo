from animal import Animal

class Pinguino(Animal):
    def __init__(self, nombre, edad, nivel_salud, nivel_felicidad):
        super().__init__(nombre, edad, nivel_salud, nivel_felicidad)