# Esta clase sera la encargada de realizar las querys a la base de datos
# Importamos clases necesarias
from repositorio import Repositorio
from alumno import Alumno

#Sin init porque lo hereda de la clase Repositorio
class RepositorioAlumno(Repositorio):

# Este metodo realiza una lista de python con todos los elementos alumnos que haya en la BD"
    def get_all(self):
        query = "SELECT dni, nombre, asistencia, tp, p1, p2, condicion, notafinal FROM alumnos"
        result = self.cursor.execute(query).fetchall()

        alumnos = []
        for r in result:
            a = Alumno(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7])
            a.cambiar_condicion()
            alumnos.append(a)
        
        return alumnos
