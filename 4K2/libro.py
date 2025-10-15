from material import Material
import math

class Libro(Material):
    def __init__(self, codigo, titulo, autor, precio_base, dias_prestados):
        super().__init__(1, codigo, titulo, autor, precio_base, dias_prestados)
        self.dias_prestados = dias_prestados

    def calcular_costo_mantenimiento(self):
        costo = 100 * (math.ceil(self.dias_prestados / 30))
        return round(costo)
    
