from abc import ABC, abstractmethod

class Material(ABC):
    def __init__(self, tipo: int, codigo: str, titulo: str, autor: str, precio_base: float, car_extra):
        self.tipo = tipo
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.precio_base = precio_base
        self.car_extra = car_extra

    @abstractmethod
    def calcular_costo_mantenimiento(self):
        pass