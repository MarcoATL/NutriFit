import sqlite3

# Función para inicializar la base de datos
def init_db():
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS usuarios
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                 nombre TEXT NOT NULL, 
                 apellidos TEXT NOT NULL, 
                 correo TEXT NOT NULL, 
                 contrasena TEXT NOT NULL)''')
    
    conn.commit()
    conn.close()

# Función para insertar un usuario en la base de datos
def insertar_usuario(nombre, apellidos, correo, contrasena):
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    
    c.execute("INSERT INTO usuarios (nombre, apellidos, correo, contrasena) VALUES (?, ?, ?, ?)", (nombre, apellidos, correo, contrasena))
    
    conn.commit()
    conn.close()

def actualizar_usuario(nombre, apellidos, correo):
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    
    c.execute("UPDATE usuarios SET nombre = ?, apellidos = ? WHERE correo = ?", (nombre, apellidos, correo))
    
    conn.commit()
    conn.close()


def verificar_credenciales(correo, contrasena):
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()

    c.execute("SELECT * FROM usuarios WHERE correo = ? AND contrasena = ?", (correo, contrasena))
    usuario = c.fetchone()

    conn.close()

    if usuario:
        # Credenciales válidas
        return True
    else:
        # Credenciales inválidas
        return False
    
def obtener_usuario_por_correo(correo):
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()

    c.execute("SELECT * FROM usuarios WHERE correo = ?", (correo,))
    usuario = c.fetchone()

    conn.close()

    # Convertir la tupla en un diccionario para facilitar el acceso a los datos en la plantilla
    if usuario:
        usuario_dict = {
            'id': usuario[0],
            'nombre': usuario[1],
            'apellidos': usuario[2],
            'correo': usuario[3],
            'contrasena': usuario[4]
        }
        return usuario_dict

# Ejemplo de uso: creación de la base de datos y registro de un usuario
#init_db()
#insertar_usuario("John", "Doe", "johndoe@example.com", "password123")
#insertar_usuario("Marco Antonio", "Torres Lopez", "marko274.matl@gmail.com", "Huesitos1")
