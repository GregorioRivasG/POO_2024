class Lectores:
    def __init__(self, nombre, direccion, tel):
        self.nombre = nombre
        self.direccion = direccion
        self.tel = tel

    def reservar(self):
        print(f"{self.nombre} ha reservado un libro.")

    def entregar(self):
        print(f"{self.nombre} ha entregado un libro.")

class Estudiantes(Lectores):
    def __init__(self, nombre, direccion, tel, carrera, matricula):
        super().__init__(nombre, direccion, tel)
        self.carrera = carrera
        self.matricula = matricula

    def reservar(self):
        print(f"El estudiante {self.nombre} con matrícula {self.matricula} ha reservado un libro.")

    def entregar(self):
        print(f"El estudiante {self.nombre} con matrícula {self.matricula} ha entregado un libro.")

class Docentes(Lectores):
    def __init__(self, nombre, direccion, tel, modalidad, num_empleado):
        super().__init__(nombre, direccion, tel)
        self.modalidad = modalidad
        self.num_empleado = num_empleado

    def reservar(self):
        print(f"El docente {self.nombre} con número de empleado {self.num_empleado} ha reservado un libro.")

    def entregar(self):
        print(f"El docente {self.nombre} con número de empleado {self.num_empleado} ha entregado un libro.")
