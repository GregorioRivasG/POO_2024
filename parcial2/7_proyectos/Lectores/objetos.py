from clases import *

def main():
    estudiante = Estudiantes("Ana Torres Guzman", "Col. Centro 1500 ote", "6181234567", "Meca", "2335678")
    estudiante.reservar()
    estudiante.entregar()

    docente = Docentes("Daniel Fuentes Loera", "Fracc.D.Arrieta 1400 nte", "6183335678", "Ti", "123")
    docente.reservar()
    docente.entregar()

if __name__ == "__main__":
    main()
