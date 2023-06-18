import sqlite3
from sqlite3 import Error

def conectar():
    try:
        conexion = sqlite3.connect('database.db')
        print('se ha conectado a la base de datos')
        return conexion
    except Error:
        print('Ha ocurrido un error')

def crear_tabla(conexion):
    cursor = conexion.cursor()
    sentencia_sql = '''CREATE TABLE IF NOT EXISTS usuario(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL)'''
    cursor.execute(sentencia_sql)
    conexion.commit()
    conexion.close()

def insertar(conexion, datos):
    cursor = conexion.cursor()
    sentencia_sql = 'INSERT INTO usuario (nombre, apellido) VALUES (?, ?)'
    cursor.execute(sentencia_sql, datos)
    conexion.commit()
    conexion.close()

def insertar_varios(conexion, datos):
    cursor = conexion.cursor()
    sentencia_sql = 'INSERT INTO usuario (nombre, apellido) VALUES (?, ?)'
    cursor.executemany(sentencia_sql, datos)
    conexion.commit()
    conexion.close()

conexion = conectar()
#crear_tabla(conexion)
datos = ('Pablo', 'España')
insertar(conexion, datos)
