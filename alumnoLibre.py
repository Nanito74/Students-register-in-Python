from alumno import Alumno

class AlumnoLibre(Alumno):
    def __init__(self, dni, nombre, asistencia=None, tp=None, p1=None, p2=None, condicion='', notafinal=None, libre= 'si'):
        self.libre = libre
        super().__init__(dni, nombre, asistencia, tp, p1, p2, condicion, notafinal)
    
    def cambiar_condicion_libre(self):
        if int(self.tp) >= 100 and int(self.p1) >= 8 and int(self.p2) >= 8:
            self.condicion = 'Aprobado'
        else:
            self.condicion = 'Desaprobado'