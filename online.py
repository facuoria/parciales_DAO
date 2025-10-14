from curso import Curso

class Online(Curso):
    def __init__(self, codigo, nombre, precio_base, cantidad_alumnos, incluye_tutorias):
        super().__init__(3, codigo, nombre, precio_base, cantidad_alumnos, incluye_tutorias)
        self.incluye_tutorias = incluye_tutorias

    def calcular_precio(self):
        base = super().calcular_precio()
        if self.incluye_tutorias:
            return base * 1.15
        return base
