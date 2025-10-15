from material import Material

class Revista(Material):
    def __init__(self, codigo, titulo, autor, precio_base, origen):
        super().__init__(3, codigo, titulo, autor, precio_base, origen)
        self.origen = origen

    def calcular_costo_mantenimiento(self):
        costo = 50
        if self.origen.lower() == "importada":
            costo *= 1.2
        return costo