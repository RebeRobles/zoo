from animal import Animal

class Jirafa(Animal):
    def __init__(self, nombre, edad, nivel_salud, nivel_felicidad):
        super().__init__(nombre, edad, nivel_salud, nivel_felicidad)
        
    def alimentacion(self, comida):
        if comida <= 4:
            self.nivel_salud += 4
            self.nivel_felicidad += 4
        elif comida <= 8:
            self.nivel_salud += 8
            self.nivel_felicidad += 8
        elif comida < 10:
            self.nivel_salud += 10
            self.nivel_felicidad += 10
        return self
