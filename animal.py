class Animal:

    def __init__(self, nombre, edad, nivel_salud, nivel_felicidad):
        self.nombre = nombre
        self.edad = edad
        self.nivel_salud = nivel_salud
        self.nivel_felicidad = nivel_felicidad
    
    def alimentacion(self):
        self.nivel_salud += 10
        self.nivel_felicidad += 10
        return self

    def display_info(self):
        return f'{self.nombre} : tiene {self.nivel_salud} de salud,  {self.nivel_felicidad} nivel de felicidad'
