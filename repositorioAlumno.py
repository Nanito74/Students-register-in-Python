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

#Este metodo recibe un alumno y lo almacena en la base de datos. Primero actualiza su condicion. Y se guardan los cambios si todo salio exitosamente. De lo contrario retorna False
    def store(self, alumno):
        alumno.cambiar_condicion()
        try: 
            query = "INSERT INTO alumnos (dni, nombre, asistencia, tp, p1, p2, condicion, notafinal) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
            self.cursor.execute(query, [alumno.dni, alumno.nombre, alumno.asistencia, alumno.tp, alumno.p1, alumno.p2, alumno            alumno.condicion, alumno.notafinal])
            self.bd.commit()
            return True
        except:
            self.bd.rollback()
            return False
#Este metodo recibe un alumno y lo elimina en la base de datos.Y se guardan los cambios si todo salio exitosamente. De lo contrario retorna False. Tambien returna False si ese alumno no existe.
    def delete(self,alumno):
        try:
            query = "DELETE FROM alumnos WHERE dni = ?"
            self.cursor.execute(query, [alumno.dni])
 
            c = self.cursor.rowcount
            if c == 0:
                self.bd.rollback()
                return False
            else:
                self.bd.commit()
                return True
        except:
            self.bd.rollback()
            return False
