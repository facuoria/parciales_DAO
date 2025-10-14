from curso import Curso

class Practico(Curso):
    def __init__(self, codigo, nombre, precio_base, cantidad_alumnos, practicas_laboratorio):
        super().__init__(2, codigo, nombre, precio_base, cantidad_alumnos, practicas_laboratorio)
        self.practicas_laboratorio = practicas_laboratorio

    def calcular_precio(self):
        return super().calcular_precio() + (500 * self.practicas_laboratorio)
