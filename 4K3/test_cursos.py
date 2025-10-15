import pytest
from universidad import Universidad
from curso import Curso
from teorico import Teorico
from practico import Practico
from online import Online

def test_constructor_universidad():
    universidad = Universidad("cursos.csv")
    assert universidad is not None
    assert universidad.cantidad_cursos() == 6

def test_constructor_archivo_inexistente():
    with pytest.raises(FileNotFoundError):
        Universidad("archivo_inexistente.csv")

def test_cantidad_por_tipo():
    universidad = Universidad("cursos.csv")
    cantidades = universidad.cantidad_por_tipo()
    assert cantidades == { "Teórico": 2, "Práctico": 2, "Online": 2 }

def test_teorico_60_alumnos():
    teorico = Teorico("T101", "Matemática I", 2000, 60)
    assert teorico.calcular_precio() == 1800
    assert teorico.calcular_precio_total() == 108000 

def test_teorico_45_alumnos():
    teorico = Teorico("T102", "Filosofía", 1800, 45)
    assert teorico.calcular_precio() == 1800
    assert teorico.calcular_precio_total() == 81000

def test_practico_5_laboratorios():
    practico = Practico("P201", "Química General", 2500, 40, 5)
    assert practico.calcular_precio() == 5000
    assert practico.calcular_precio_total() == 200000

def test_practico_3_laboratorios():
    practico = Practico("P202", "Electrónica", 2700, 35, 3)
    assert practico.calcular_precio() == 4200
    assert practico.calcular_precio_total() == 147000

def test_online_con_tutorias():
    online = Online("O301", "Programación en Python", 2200, 80, True)
    assert online.calcular_precio() == 2530
    assert online.calcular_precio_total() == 202400

def test_online_sin_tutorias():
    online = Online("O302", "Inglés Técnico", 2000, 50, False)
    assert online.calcular_precio() == 2000
    assert online.calcular_precio_total() == 100000

def test_calcular_promedio_precio_por_estudiante():
    universidad = Universidad("cursos.csv")
    promedio = universidad.calcular_promedio_precio_por_estudiante()
    assert promedio == 2483

def test_curso_mas_caro():
    universidad = Universidad("cursos.csv")
    curso_caro = universidad.obtener_curso_mas_caro()
    assert curso_caro.codigo == "P201"
    assert curso_caro.nombre == "Química General"
    assert curso_caro.calcular_precio() == 5000

def test_ingreso_total():
    universidad = Universidad("cursos.csv")
    ingreso_total = universidad.calcular_ingreso_total()
    assert ingreso_total == 1018400

def test_contar_teoricos_mas_50_alumnos():
    universidad = Universidad("cursos.csv")
    teoricos_mas_50 = universidad.contar_teoricos_mas_50_alumnos()
    assert teoricos_mas_50 == 1

def test_contar_online_con_tutorias():
    universidad = Universidad("cursos.csv")
    online_con_tutorias = universidad.contar_online_con_tutorias()
    assert online_con_tutorias == 1

def test_herencia_cursos():
    assert issubclass(Teorico, Curso)
    assert issubclass(Practico, Curso)
    assert issubclass(Online, Curso)

def test_composicion_universidad_cursos():
    universidad = Universidad("cursos.csv")
    assert hasattr(universidad, 'cursos')
    for curso in universidad.cursos:
        assert isinstance(curso, Curso)

def test_atributos_teorico():
    teorico = Teorico("T101", "Matemática I", 2000, 60)
    assert teorico.tipo == 1
    assert teorico.codigo == "T101"
    assert teorico.nombre == "Matemática I"
    assert teorico.precio_base == 2000
    assert teorico.cantidad_alumnos == 60

def test_atributos_practico():
    practico = Practico("P201", "Química General", 2500, 40, 5)
    assert practico.tipo == 2
    assert practico.practicas_laboratorio == 5

def test_atributos_online():
    online = Online("O301", "Programación en Python", 2200, 80, True)
    assert online.tipo == 3
    assert online.incluye_tutorias == True
