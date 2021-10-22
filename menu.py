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