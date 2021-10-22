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
        self.b4=ttk.Button(self.ventana, text ="Modificar alumno",command=lambda:[self.limpiarmarcos(self.marco4)])
        self.b4.grid(row=0,column=3)
        self.b5=ttk.Button(self.ventana, text ="Buscar alumno",command=lambda:[self.limpiarmarcos(self.marco5)])
        self.b5.grid(row=0,column=4)
        self.b6 = ttk.Button(self.ventana, text ="Buscar por condicion",command=lambda:[self.limpiarmarcos(self.marco6)])
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
        self.marco2.grid(row= 0, column=8, columnspan= 2)
        self.marco2.grid_remove()
        botonagregar = ttk.Button(self.marco2,text='Agregar',command=self.agregar).grid(row=6, column=1)
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
        Label(self.marco2,text='Parcial 2').grid(row=4,column=0)
        self.p2=Entry(self.marco2)
        self.p2.grid(row=5,column=1)
        Label(self.marco2,text='Libre').grid(row=5,column=0)
        self.libre=Entry(self.marco2)
        self.libre.grid(row=6,column=1)

#Aca ejecutamos el menu automaticamente
if __name__ == "__main__":
    ventana= Tk()
    aplicacion=Menu(ventana)
    ventana.mainloop()