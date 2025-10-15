from material import Material
from libro import Libro
from ebook import Ebook
from revista import Revista
from collections import defaultdict
import csv

class Biblioteca:
    def __init__(self, archivo_csv: str):
        self.materiales = []
        self.cargar_materiales(archivo_csv)

    # 1. Cargar materiales desde el archivo.
    def cargar_materiales(self, archivo_csv):
        try:
            with open(archivo_csv, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                for fila in reader:
                    try:
                        tipo = int(fila[0])
                        codigo = fila[1]
                        titulo = fila[2]
                        autor = fila[3]
                        precio_base = float(fila[4])
                        car_extra = fila[5].strip()

                        if tipo == 1:
                            dias_prestados = int(car_extra)
                            material = Libro(codigo, titulo, autor, precio_base, dias_prestados)
                        elif tipo == 2:
                            valor_venta = int(car_extra)
                            material = Ebook(codigo, titulo, autor, precio_base, valor_venta)
                        elif tipo == 3:
                            origen = car_extra.lower()
                            material = Revista(codigo, titulo, autor, precio_base, origen)
                        else:
                            print(f"Tipo desconocido ({tipo}) en fila: {fila}")
                            continue

                        self.materiales.append(material)
                    except (ValueError, IndexError) as e:
                        print(f"Error procesando fila {fila}: {e}")
        except FileNotFoundError as e:
            print(f"No se encontró el archivo: {archivo_csv}")
            raise e
        except Exception as e:
            print(f"Error inesperado al leer el archivo: {e}")

    def listar_materiales(self):
        for material in self.materiales:
            print(f"{material.codigo} ({material.__class__.__name__}) - Mantenimiento: ${material.calcular_costo_mantenimiento()}")

    def cantidad_materiales(self):
        return self.materiales
    
    # 2. Calcular el promedio entero de los precios base de todos.
    def calcular_promedio_precios_base(self):
        acumulado = cantidad = promedio = 0
        for material in self.materiales:
            acumulado += material.precio_base
            cantidad += 1
        promedio = acumulado // cantidad
        return promedio

    # 3. Obtener el material con mayor costo de mantenimiento.
    def obtener_material_mayor_costo_mantenimiento(self):
        mayor_costo = self.materiales[0]
        for material in self.materiales:
            if material.calcular_costo_mantenimiento() > mayor_costo.calcular_costo_mantenimiento():
                mayor_costo = material
        return mayor_costo
    
    def mostrar_material_mayor_costo_mantenimiento(self):
        mayor_costo = self.materiales[0]
        for material in self.materiales:
            if material.calcular_costo_mantenimiento() > mayor_costo.calcular_costo_mantenimiento():
                mayor_costo = material
        return mayor_costo.calcular_costo_mantenimiento()
    
    # 4. Calcular la suma de costo de mantenimiento de todos los préstamos.
    def calcular_suma_costo_mantenimiento(self):
        suma = 0
        for material in self.materiales:
            suma += material.calcular_costo_mantenimiento()
        return suma
    
    # 5. Contar cuántos libros físicos se prestaron por más de 30 días.
    def contar_libros_mas_30_dias(self):
        cantidad = 0
        for material in self.materiales:
            if material.tipo == 1:
                if material.dias_prestados > 30:
                    cantidad += 1
        return cantidad

    # 6. Contar cuántas revistas son importadas.
    def contar_revistas_importadas(self):
        cantidad = 0
        for material in self.materiales:
            if material.tipo == 3:
                if material.origen.lower() == "importada":
                    cantidad += 1
        return cantidad
    
    # 7. Calcular en un diccionario la cantidad de materiales de cada tipo, las claves del diccionario deben ser "Libro", "Ebook" y "Revista".
    def cantidad_por_tipo(self):
        conteo = { 
            "Libro": 0, 
            "Ebook": 0, 
            "Revista": 0 
        }
        for material in self.materiales:
            if isinstance(material, Libro):
                conteo["Libro"] += 1
            elif isinstance(material, Ebook):
                conteo["Ebook"] += 1
            elif isinstance(material, Revista):
                conteo["Revista"] += 1
        return conteo

if __name__ == "__main__":
    biblioteca = Biblioteca("material.csv")
    print()
    biblioteca.listar_materiales()
    print("-----------------------------------")
    print(f"Promedio de precios base: {biblioteca.calcular_promedio_precios_base()}")
    print(f"Mantenimiento más caro: {biblioteca.mostrar_material_mayor_costo_mantenimiento()}")
    print(f"Suma de mantenimientos: {biblioteca.calcular_suma_costo_mantenimiento()}")
    print(f"Libros prestados +30 días: {biblioteca.contar_libros_mas_30_dias()}")
    print(f"Revistas importadas: {biblioteca.contar_revistas_importadas()}")
    print(biblioteca.cantidad_por_tipo())
