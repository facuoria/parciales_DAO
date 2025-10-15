from curso import Curso

class Teorico(Curso):
    def __init__(self, codigo, nombre, precio_base, cantidad_alumnos, extra=0):
        super().__init__(1, codigo, nombre, precio_base, cantidad_alumnos, extra)

    def calcular_precio(self):
        base = super().calcular_precio()
        if self.cantidad_alumnos > 50:
            return base * 0.9
        return base
