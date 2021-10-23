#Importaciones necesarias para el menu y la interfaz grafica.

from sqlite3.dbapi2 import Row
import sys
from tkinter.constants import CENTER, END
from registro import Registro
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb

#Definimos la clase Menu, la cual recibira una ventana que sera la que usaremos para trabajar en tkinter

class Menu:

    def __init__(self,ventana):
        self.registro = Registro()
        self.ventana = ventana
        self.ventana.title('Proyecto de registro')
        self.ventana.geometry('1280x720')

#Aca diseñamos el menú a base de botones, y cada uno tendrá el comando de mostrar su marco correspondiente
        self.b1 = ttk.Button(self.ventana, text ="Mostrar registro",command=lambda:[self.limpiarmarcos(self.marco1),self.mostrar_registro()])
        self.b1.grid(row=0,column=0)
        self.b2 = ttk.Button(self.ventana, text ="Nuevo alumno",command=lambda:[self.limpiarmarcos(self.marco2)])
        self.b2.grid(row=0,column=1)
        self.b3 = ttk.Button(self.ventana, text ="Eliminar alumno",command=lambda:[self.limpiarmarcos(self.marco3)])
        self.b3.grid(row=0,column=2)
        self.b4=ttk.Button(self.ventana, text ="Buscar por condicion",command=lambda:[self.limpiarmarcos(self.marco4)])
        self.b4.grid(row=0,column=3)
        self.b5=ttk.Button(self.ventana, text ="Modificar alumno",command=lambda:[self.limpiarmarcos(self.marco5)])
        self.b5.grid(row=0,column=4)
        self.b6 = ttk.Button(self.ventana, text ="Buscar alumno",command=lambda:[self.limpiarmarcos(self.marco6)])
        self.b6.grid(row=0,column=5)
        self.b7 = ttk.Button(self.ventana, text ="Salir",command=self.salir).grid(row=0,column=6)

#Aca disenaremos la tabla, la cual usaremos para mostrar el registro completo, o con las condiciones correspondientes
        self.marco1 = LabelFrame(self.ventana,text='Registro')
        self.marco1.grid(row=2,column=0,columnspan=1000)
        self.marco1.grid_remove()
        
        self.tabla = ttk.Treeview(self.marco1,columns= ('c1', 'c2','c3', 'c4', 'c5', 'c6', 'c7', 'c8'))
        self.tabla.column('#0',anchor=CENTER)
        self.tabla.column('c1',anchor=CENTER)
        self.tabla.column('c2',anchor=CENTER)
        self.tabla.column('c3',anchor=CENTER)
        self.tabla.column('c4',anchor=CENTER)
        self.tabla.column('c5',anchor=CENTER)
        self.tabla.column('c6',anchor=CENTER)
        self.tabla.column('c7',anchor=CENTER)
        self.tabla.column('c8',anchor=CENTER)
        self.tabla.grid(row=2,column=0)
       
        self.tabla.heading('#0',text='DNI')
        self.tabla.heading('c1',text='Nombre')
        self.tabla.heading('c2',text='Asistencia')
        self.tabla.heading('c3',text='Tps')
        self.tabla.heading('c4',text='Parcial 1')
        self.tabla.heading('c5',text='Parcial 2')
        self.tabla.heading('c6',text='Condicion')
        self.tabla.heading('c7',text='Nota Final')
        self.tabla.heading('c8',text='Libre')

#Crearemos la interfaz que usaremos para agregar un alumno al registro. Ademas tendra un boton que asignara los cambios.    
        self.marco2 = LabelFrame(self.ventana, text='Nuevo alumno')
        self.marco2.grid(row= 2, column=9, columnspan= 2)
        self.marco2.grid_remove()
        botonagregar = ttk.Button(self.marco2,text='Agregar',command=self.agregar).grid(row=7, column=1)
        Label(self.marco2,text='DNI').grid(row=0,column=0)
        self.dni=Entry(self.marco2)
        self.dni.grid(row=0,column=1)
        Label(self.marco2,text='Nombre').grid(row=1,column=0)
        self.nombre=Entry(self.marco2)
        self.nombre.grid(row=1,column=1)
        Label(self.marco2,text='Asistencia').grid(row=2,column=0)
        self.asistencia=Entry(self.marco2)
        self.asistencia.grid(row=2,column=1)
        Label(self.marco2,text='Tps').grid(row=3,column=0)
        self.tp= Entry(self.marco2)
        self.tp.grid(row=3,column=1)
        Label(self.marco2,text='Parcial 1').grid(row=4,column=0)
        self.p1=Entry(self.marco2)
        self.p1.grid(row=4,column=1)
        Label(self.marco2,text='Parcial 2').grid(row=5,column=0)
        self.p2=Entry(self.marco2)
        self.p2.grid(row=5,column=1)
        Label(self.marco2,text='Libre (Escriba "si" en miniscula por favor').grid(row=6,column=0)
        self.libre=Entry(self.marco2)
        self.libre.grid(row=6,column=1)

#Aca produciremos la interfaz de eliminado de alumno con su boton para realizar la accion.
        self.marco3 = LabelFrame(self.ventana, text='Eliminar alumno')
        self.marco3.grid(row= 1, column=8)
        self.marco3.grid_remove()
        botoneliminar = ttk.Button(self.marco3,text='Eliminar',command=lambda:[self.eliminar()]).grid(row=6, column=1)
        Label(self.marco3,text='DNI').grid(row=0,column=8)
        self.dnidelete = Entry(self.marco3)
        self.dnidelete.grid(row=0,column=1)

#Aca produciremos la interfaz para buscar a un alumno por su condicion, ya sea aprobado, desaprobado, regular, incompleto
        self.marco4 = LabelFrame(self.ventana,text='Buscar por condicion')
        self.marco4.grid(row=1, column=8)
        self.marco4.grid_remove()
        Label(self.marco4,text='Condicion').grid(row=0,column=8)
        self.condicion = Entry(self.marco4)
        self.condicion.grid(row=0,column=1)
        botonbuscar = ttk.Button(self.marco4,text='Buscar',command=lambda:[self.buscar_condicion(), self.limpiarmarcos(self.marco1)]).grid(row=6, column=1)

#Realizamos la interfaz para modificar un alumno.
        self.marco5 = LabelFrame(self.ventana, text='Modificar alumno')
        self.marco5.grid(row= 2, column=9, columnspan= 2)
        self.marco5.grid_remove()
        botonmodificar = ttk.Button(self.marco5,text='Modificar',command=lambda:[self.modificar()]).grid(row=7, column=1)
        Label(self.marco5,text='Dni').grid(row=0,column=0)
        self.dniviejo=Entry(self.marco5)
        self.dniviejo.grid(row=0,column=1)
        Label(self.marco5,text='Nuevo Dni').grid(row=1,column=0)
        self.nuevodni=Entry(self.marco5)
        self.nuevodni.grid(row=1,column=1)
        Label(self.marco5,text='Nombre').grid(row=2,column=0)
        self.nuevonombre=Entry(self.marco5)
        self.nuevonombre.grid(row=2,column=1)
        Label(self.marco5,text='Asistencia').grid(row=3,column=0)
        self.nuevaasistencia=Entry(self.marco5)
        self.nuevaasistencia.grid(row=3,column=1)
        Label(self.marco5,text='Tps').grid(row=4,column=0)
        self.nuevotp= Entry(self.marco5)
        self.nuevotp.grid(row=4,column=1)
        Label(self.marco5,text='Parcial 1').grid(row=5,column=0)
        self.nuevop1=Entry(self.marco5)
        self.nuevop1.grid(row=5,column=1)
        Label(self.marco5,text='Parcial 2').grid(row=6,column=0)
        self.nuevop2=Entry(self.marco5)
        self.nuevop2.grid(row=6,column=1)

#Por ultimo realizaremos la interfaz para buscar a un alumno por su nombre o DNI
        self.marco6 = LabelFrame(self.ventana, text='Buscar alumno por nombre o DNI (Distingue mayusculas)')
        self.marco6.grid(row= 2, column=8)
        self.marco6.grid_remove()
        Label(self.marco6,text='DNI/Nombre').grid(row=4,column=0)
        self.filtro = Entry(self.marco6)
        self.filtro.grid(row=4,column=1)
        botonbuscaralumno = ttk.Button(self.marco6,text='Buscar',command=lambda:[self.buscar_alumno(), self.limpiarmarcos(self.marco1)]).grid(row=6, column=1)

#Estos metodos se utilizaran para limpiar la interfaz de usuario y actualizarla cuando sea necesario.
    def limpiarmarcos(self, marco):
        self.marco1.grid_remove()
        self.marco2.grid_remove()
        self.marco3.grid_remove()
        self.marco4.grid_remove()
        self.marco5.grid_remove()
        self.marco6.grid_remove()
 
        self.marco = marco
        self.marco.grid()
    
    def limpiarcampos(self):
        self.nombre.delete(0,END)
        self.dni.delete(0,END)
        self.asistencia.delete(0,END)
        self.tp.delete(0,END)
        self.p1.delete(0,END)
        self.p2.delete(0,END)
        self.libre.delete(0,END)
        self.dnidelete.delete(0,END)
        self.condicion.delete(0,END)
        self.dniviejo.delete(0,END)
        self.nuevodni.delete(0,END)
        self.nuevonombre.delete(0,END)
        self.nuevaasistencia.delete(0,END)
        self.nuevotp.delete(0,END)
        self.nuevop1.delete(0,END)
        self.nuevop2.delete(0,END)
        self.filtro.delete(0,END)


#Metodo de mostrar registro. Muestra un registro condicionado si lo obtiene y si no muestra el registro total. Inserta los datos en la  tabla
    def mostrar_registro(self, alumnos=None):
            self.tabla.delete(*self.tabla.get_children())
            if alumnos:
                for alumno  in alumnos:
                    self.tabla.insert("",END,text=alumno.dni,values=(alumno.nombre, alumno.asistencia, alumno.tp, alumno.p1, alumno.p2, alumno.condicion, alumno.notafinal, alumno.libre))
            else:
                for alumno in self.registro.alumnos:
                    self.tabla.insert("",END,text=alumno.dni,values=(alumno.nombre, alumno.asistencia, alumno.tp, alumno.p1, alumno.p2, alumno.condicion, alumno.notafinal, alumno.libre))

#Metodo para agregar alumno. Recibe los entrys de la interfaz y almacena los datos. Si es libre almacena alumno libre. Si dni o nombre no estan completados muestra error
    def agregar(self):
        dni = self.dni.get()
        nombre = self.nombre.get()
        if len(dni) != 0 and len(nombre) != 0:
            asistencia = self.asistencia.get()
            if asistencia == '':
                asistencia = None
            tp = self.tp.get()
            if tp == '':
                tp = None
            p1 = self.p1.get()
            if p1 == '':
                p1 = None
            p2 = self.p2.get()
            if p2 == '':
                p2 = None
            libre = self.libre.get()
            if libre == 'si':
                alumnos = self.registro.nuevo_alumno_libre(dni,nombre,asistencia,tp,p1,p2,libre)
                self.limpiarcampos
                mb.showinfo('Exito','Alumno cargado exitosamente')                
            else: 
                alumnos = self.registro.nuevo_alumno(dni,nombre,asistencia,tp,p1,p2)
                self.limpiarcampos()                
                mb.showinfo('Exito','Alumno cargado exitosamente')
        else:
            mb.showerror('Error','Debes cargar estos campos!')
            self.limpiarcampos()

#Este metodo obtendra los datos del entry de la interfaz y modificara los datos. Si se modifica con exito retorna un mensaje.
    def modificar(self):
        dni = int(self.dniviejo.get())
        nuevodni = self.nuevodni.get()
        nombre = self.nuevonombre.get()
        asistencia = self.nuevaasistencia.get()
        tp = self.nuevotp.get()
        p1 = self.nuevop1.get()
        p2 = self.nuevop2.get()
        if self.registro.modificar_alumno(dni,nuevodni,nombre,asistencia,tp,p1,p2):
            mb.showinfo('Exito','Alumno modificado con exitosamente')
            self.limpiarcampos()
        else:
            mb.showerror('Error',('Ha ocurrido un error, asegurate de que el alumno exista'))
            self.limpiarcampos()
#Metodo eliminar alumno. Recibe un dni y elimina al alumno del registro.
    def eliminar(self):
        dni = int(self.dnidelete.get())
        if self.registro.eliminar_alumno(dni):
            self.limpiarcampos()
            mb.showinfo('Exito','Alumno eliminado exitosamente')
        else:
            mb.showerror('Error','Alumno no encontrado')
            self.limpiarcampos()

#Este metodo busca alumno por filtro DNI O Nombre y retorna una lista con las coincidencias. Si no muestra error.
    def buscar_alumno(self):
        filtro = self.filtro.get()
        alumnos = self.registro.buscar(filtro)
        if alumnos:
            self.mostrar_registro(alumnos)
            self.limpiarcampos()
        else:
            mb.showerror('Error','Ningun alumno coincide con el filtro')
            self.limpiarcampos()

#Este metodo busca alumno por condicion y retorna una lista con las coincidencia. Si no muestra error.
    def buscar_condicion(self):
        condicion = self.condicion.get()
        alumnos = self.registro.mostrar_condicion(condicion)
        if alumnos:
            self.mostrar_registro(alumnos)
            self.limpiarcampos()
        else:
            mb.showerror('Error','Ningun alumno coincide con la condicion')
            self.limpiarcampos()

#Salir del sistema
    def salir(self):
        sys.exit(0)


#Aca ejecutamos el menu automaticamente
if __name__ == "__main__":
    ventana= Tk()
    aplicacion=Menu(ventana)
    ventana.mainloop()