from animal import Animal

class Leon(Animal):
    def __init__(self, nombre, edad, nivel_salud, nivel_felicidad, melena):
        super().__init__(nombre, edad, nivel_salud, nivel_felicidad)
        self.melena = melena
        
    def alimentacion(self, comida):
        if comida <= 5:
            self.nivel_salud += 5
            self.nivel_felicidad += 5
        elif comida <= 10:
            self.nivel_salud += 10
            self.nivel_felicidad += 10
        elif comida < 20:
            self.nivel_salud += 15
            self.nivel_felicidad += 15
        return self




