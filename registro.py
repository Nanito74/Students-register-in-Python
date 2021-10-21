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