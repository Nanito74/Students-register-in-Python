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