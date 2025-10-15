class Curso:
    def __init__(self, tipo: int, codigo: str, nombre: str, precio_base: float, cantidad_alumnos: int, extra):
        self.tipo = tipo
        self.codigo = codigo
        self.nombre = nombre
        self.precio_base = precio_base
        self.cantidad_alumnos = cantidad_alumnos
        self.extra = extra

    def calcular_precio(self):
        return self.precio_base
    
    def calcular_precio_total(self):
        total = self.calcular_precio() * self.cantidad_alumnos
        return total
    