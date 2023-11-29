import sqlite3

# Configuración de conexión
db_path = 'tunetalk.db'  # Cambia 'tu_database.db' al nombre que desees para tu archivo SQLite

# Verificar la conexión al importar este módulo
def check_database_connection():
    try:
        conn = sqlite3.connect(db_path)
        print("Conexión a la base de datos establecida correctamente.")
        conn.close()
        return True
    except sqlite3.Error as e:
        print(f"Error de conexión a la base de datos: {e}")
        return False
    
# Insertar usuario
def insert_user_into_database(id_usuario, nombre, edad):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Crear la tabla 'usuario' si no existe
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuario (
                idusuario TEXT PRIMARY KEY,
                nombre TEXT,
                edad INTEGER
            )
        ''')

        # Insertar el usuario en la tabla 'usuario'
        query = "INSERT INTO usuario (idusuario, nombre, edad) VALUES (?, ?, ?)"
        data = (id_usuario, nombre, edad)
        cursor.execute(query, data)

        # Confirmar la transacción y cerrar la conexión
        conn.commit()
        conn.close()

        return True
    except sqlite3.Error as e:
        print(f"Error al insertar usuario en la base de datos: {e}")
        return False

# Actualizar Usuario    
def update_user_in_database(id_usuario, nuevo_nombre, nueva_edad):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Verificar si el usuario existe en la base de datos
        cursor.execute("SELECT * FROM usuario WHERE idusuario=?", (id_usuario,))
        existing_user = cursor.fetchone()

        if existing_user:
            # Actualizar el nombre y la edad del usuario
            cursor.execute("UPDATE usuario SET nombre=?, edad=? WHERE idusuario=?", (nuevo_nombre, nueva_edad, id_usuario))

            # Confirmar la transacción y cerrar la conexión
            conn.commit()
            conn.close()

            return True
        else:
            print("Usuario no encontrado en la base de datos.")
            return False
    except sqlite3.Error as e:
        print(f"Error al actualizar usuario en la base de datos: {e}")
        return False
    
# Crear tabla 'generos'
def create_generos_table():
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS generos (
                nombre_genero TEXT PRIMARY KEY,
                playlist TEXT
            )
        ''')

        # Insertar los 10 géneros más populares
        generos_populares = [
            ("Pop", "https://open.spotify.com/playlist/37i9dQZF1DWSpF87bP6JSF?si=172a45b2c78445a5"),
            ("Rock", "https://open.spotify.com/playlist/37i9dQZF1DXcF6B6QPhFDv?si=a08f4fc11a514d4e"),
            ("Hip Hop", "https://open.spotify.com/playlist/37i9dQZF1DWVA1Gq4XHa6U?si=ac586153956c4084"),
            ("Banda", "https://open.spotify.com/playlist/37i9dQZF1DX905zIRtblN3?si=40dc9c914ce24f8f"),
            ("Electronica", "https://open.spotify.com/playlist/574gu0rKWEABHngdcdYSbJ?si=9f9e6ba82e5a468c"),
            # Agrega los demás géneros populares aquí
        ]

        cursor.executemany("INSERT INTO generos (nombre_genero, playlist) VALUES (?, ?)", generos_populares)

        conn.commit()
        conn.close()

        return True
    except sqlite3.Error as e:
        print(f"Error al crear la tabla 'generos': {e}")
        return False

# Funciones para obtener opciones y playlist de géneros
def obtener_opciones_generos():
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Obtener nombres de géneros desde la tabla 'generos'
        cursor.execute("SELECT nombre_genero FROM generos")
        generos = [row[0] for row in cursor.fetchall()]

        conn.close()
        return generos
    except sqlite3.Error as e:
        print(f"Error al obtener opciones de géneros: {e}")
        return []

def obtener_playlist_genero(nombre_genero):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Obtener playlist del género seleccionado desde la tabla 'generos'
        cursor.execute("SELECT playlist FROM generos WHERE nombre_genero=?", (nombre_genero,))
        playlist = cursor.fetchone()

        conn.close()
        return playlist[0] if playlist else None
    except sqlite3.Error as e:
        print(f"Error al obtener playlist del género: {e}")
        return None

# Resto del código...