# La clase alumno permitira instaciar alumnos que contengan DNI, nombre, asistencia, tp, p1, p2, condicion y nota final.

class Alumno:
    def __init__(self, dni, nombre, asistencia, tp=None, p1=None, p2=None, condicion='', notafinal=None):
        self.dni = dni
        self.nombre = nombre
        self.asistencia = asistencia
        self.tp = tp
        self.p1 = p1
        self.p2 = p2
        self.condicion = condicion
        self.notafinal = notafinal
