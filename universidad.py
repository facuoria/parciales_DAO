import csv
from curso import Curso
from teorico import Teorico
from practico import Practico
from online import Online
from collections import defaultdict

class Universidad:
    def __init__(self, archivo_csv: str):
        self.cursos = []
        self.cargar_cursos(archivo_csv)

    def cargar_cursos(self, archivo_csv):
        with open(archivo_csv, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for fila in reader:
                tipo = int(fila[0])
                codigo = fila[1]
                nombre = fila[2]
                precio_base = float(fila[3])
                cantidad_alumnos = int(fila[4])
                extra = fila[5].strip()

                if tipo == 1:
                    extra = 0
                elif tipo == 2:
                    extra = int(extra)
                else:
                    extra = extra.lower() == "true"

                if tipo == 1:
                    curso = Teorico(codigo, nombre, precio_base, cantidad_alumnos, extra)
                elif tipo == 2:
                    curso = Practico(codigo, nombre, precio_base, cantidad_alumnos, extra)
                else:
                    curso = Online(codigo, nombre, precio_base, cantidad_alumnos, extra)

                self.cursos.append(curso)

    def listar_cursos(self):
        for curso in self.cursos:
            print(f"Curso {curso.codigo} ({curso.__class__.__name__}) - Precio: {curso.calcular_precio_total()}")

    def cantidad_cursos(self):
        return len(self.cursos)
    
    def calcular_promedio_precio_por_estudiante(self):
        monto = cantidad = promedio = 0
        for curso in self.cursos:
            monto += curso.calcular_precio() * curso.cantidad_alumnos
            cantidad += curso.cantidad_alumnos
        promedio = monto // cantidad
        return promedio

    def obtener_curso_mas_caro(self):
        mas_caro = self.cursos[0]
        for curso in self.cursos:
            if curso.calcular_precio() > mas_caro.calcular_precio():
                mas_caro = curso
        return mas_caro

    def obtener_curso_mas_caro_monto(self):
        mas_caro = self.cursos[0]
        for curso in self.cursos:
            if curso.calcular_precio() > mas_caro.calcular_precio():
                mas_caro = curso
        return mas_caro.calcular_precio()  

    def calcular_ingreso_total(self):
        total = 0
        for curso in self.cursos:
            total += curso.calcular_precio_total()
        return total
    
    def contar_teoricos_mas_50_alumnos(self):
        cantidad = 0
        for curso in self.cursos:
            if curso.tipo == 1:
                if curso.cantidad_alumnos > 50:
                    cantidad += 1
        return cantidad

    def contar_online_con_tutorias(self):
        cantidad = 0
        for curso in self.cursos:
            if curso.tipo == 3:
                if curso.incluye_tutorias:
                    cantidad += 1
        return cantidad
    
    def cantidad_por_tipo(self):
        conteo = {
            "Teórico": 0,
            "Práctico": 0,
            "Online": 0
        }
        for curso in self.cursos:
            if isinstance(curso, Teorico):
                conteo["Teórico"] += 1
            elif isinstance(curso, Practico):
                conteo["Práctico"] += 1
            elif isinstance(curso, Online):
                conteo["Online"] += 1
        return conteo


if __name__ == "__main__":
    universidad = Universidad("cursos.csv")
    print()
    universidad.listar_cursos()
    print()
    print(universidad.cantidad_cursos())
    print()
    print(universidad.calcular_promedio_precio_por_estudiante())
    print()
    print(universidad.obtener_curso_mas_caro_monto())
    print()
    print(universidad.calcular_ingreso_total())
    print()
    print(universidad.contar_teoricos_mas_50_alumnos())
    print()
    print(universidad.contar_online_con_tutorias())
    print()
    print(universidad.cantidad_por_tipo())