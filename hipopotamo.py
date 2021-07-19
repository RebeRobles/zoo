from animal import Animal

class Hipopotamo(Animal):
    def __init__(self, nombre, edad, nivel_salud, nivel_felicidad):
        super().__init__(nombre, edad, nivel_salud, nivel_felicidad)
        
    def alimentacion(self, comida):
        if comida <= 7:
            self.nivel_salud += 7
            self.nivel_felicidad += 7
        elif comida <= 13:
            self.nivel_salud += 13
            self.nivel_felicidad += 13
        elif comida < 20:
            self.nivel_salud += 15
            self.nivel_felicidad += 15
        return self
