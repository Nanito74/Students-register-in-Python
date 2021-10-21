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

#Este metodo lo crearemos para que el alumno cambie la condición automáticamente al saber sus notas y asistencia.
#Si falta alguna nota dejaremos su condicion como incompleto
 
    def cambiar_condicion(self):
        if self.asistencia is None or self.tp is None or self.p1 is None or self.p2 is None:
            self.condicion = 'Incompleto' 
        elif int(self.asistencia) >= 75 and int(self.tp) < 100 and int(self.p1) >= 8 and int(self.p2) >= 8:
            self.condicion = 'Aprobado'
        elif int(self.asistencia) >= 75 and int(self.tp) < 100 and int(self.p1) >= 6 or int(self.p2) >= 6:
            self.condicion = 'Regular'
        else:
            self.condicion = 'Desaprobado'