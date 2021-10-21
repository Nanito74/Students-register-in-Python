#Esta clase sera la encargada de coordinar la BD con el registro de memoria y tambien de interactuar con la interfaz para realizar todas las funciones
 
from alumno import Alumno
from repositorioAlumno import RepositorioAlumno
class Registro:
    
#Inciamos el repositorio y traemos todos los alumnos de la BD y los guardamos"    
    def __init__(self):
        self.repo = RepositorioAlumno()
        self.alumnos = self.repo.get_all()
    
#Creamos un alumno y lo guardamos tanto en memoria como en BD
    def nuevo_alumno(self,dni,nombre,asistencia,tp,p1,p2):
        a = Alumno(dni,nombre,asistencia,tp,p1,p2)
        self.repo.store(a)
        self.alumnos.append(a)

#Recibe un dni para buscar alumnos. Este metodo se utilizara dentro de esta clase

    def _buscar_por_dni(self, dni):
        for alumno in self.alumnos:
            if alumno.dni == dni:
                return alumno
        return None
    
#Este metodo recibe un dni, identifica si hay un alumno con ese DNI y lo elimina.

    def eliminar_alumno(self, dni):
        alumno = self._buscar_por_dni(dni)
        if alumno:
            self.repo.delete(alumno)
            self.alumnos.remove(alumno)
            return True
        return False

#Metodo para buscar por DNI o nombre en la lista de alumnos y retornar todas las coincidencias en una lista.
    def buscar(self, filtro):
        alumnos = []
        for alumno in self.alumnos:
            if alumno.buscar_alumno(filtro):
                alumnos.append(alumno)
        return alumnos
