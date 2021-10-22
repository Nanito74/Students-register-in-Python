# Esta clase sera la encargada de realizar las querys a la base de datos
# Importamos clases necesarias
from alumnoLibre import AlumnoLibre
from repositorio import Repositorio
from alumno import Alumno

#Sin init porque lo hereda de la clase Repositorio
class RepositorioAlumno(Repositorio):

# Este metodo realiza una lista de python con todos los elementos alumnos que haya en la BD"
    def get_all(self):
        query = "SELECT dni, nombre, asistencia, tp, p1, p2, condicion, notafinal, libre FROM alumnos"
        result = self.cursor.execute(query).fetchall()

        alumnos = []
        for r in result:
            if r[8] == 'si':
                a = AlumnoLibre(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7],r[8])
                a.cambiar_condicion_libre()
                alumnos.append(a)
            else:
                a = Alumno(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7])
                a.cambiar_condicion()
                alumnos.append(a)
        
        return alumnos

#Este metodo recibe un alumno y lo almacena en la base de datos. Primero actualiza su condicion. Y se guardan los cambios si todo salio exitosamente. De lo contrario retorna False
    def store(self, alumno):
        if alumno.libre:
            alumno.cambiar_condicion_libre()
        else:
            alumno.cambiar_condicion()
        try: 
            query = "INSERT INTO alumnos (dni, nombre, asistencia, tp, p1, p2, condicion, notafinal, libre) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
            self.cursor.execute(query, [alumno.dni, alumno.nombre, alumno.asistencia, alumno.tp, alumno.p1, alumno.p2, alumno.condicion, alumno.notafinal, alumno.libre])
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

#Este meotodo recibe un alumno, actualiza su condicion y actualiza sus datos en la BD. Retorna True si la actualizacion no tuvo fallos. De lo contrario retorna False. Si el alumno no existe retorna False.
    
    def update(self, alumno):
        if alumno.libre:
            alumno.cambiar_condicion_libre()
        else:
            alumno.cambiar_condicion()
        try:
            query = "UPDATE alumnos SET dni = ?, nombre = ?, asistencia = ?, tp = ?, p1 = ?, p2 = ?, condicion = ?, notafinal = ? WHERE dni = ?"
            result = self.cursor.execute(query, [alumno.nuevodni, alumno.nombre, alumno.asistencia, alumno.tp, alumno.p1, alumno.p2, alumno.condicion, alumno.notafinal, alumno.dni])
            if result.rowcount == 0:
                self.bd.rollback()
                return False
            else:
                self.bd.commit()
                return True
        except:
            self.bd.rollback()
            return False