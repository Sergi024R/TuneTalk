import mysql.connector

# Configuración de conexión
config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'tunetalk',
    'raise_on_warnings': True,
}

def check_database_connection():
    try:
        conn = mysql.connector.connect(**config)
        print("Conexión a la base de datos establecida correctamente.")
        conn.close()
        return True
    except mysql.connector.Error as e:
        print(f"Error de conexión a la base de datos: {e}")
        return False

# Verificar la conexión al importar este módulo
check_database_connection()


# Insertar usuario
def insert_user_into_database(id_usuario, nombre, edad):
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        # Insertar el usuario en la tabla 'usuario'
        query = "INSERT INTO usuario (idusuario, nombre, edad) VALUES (%s, %s, %s)"
        data = (id_usuario, nombre, edad)
        cursor.execute(query, data)

        # Confirmar la transacción y cerrar la conexión
        conn.commit()
        conn.close()

        return True
    except mysql.connector.Error as e:
        print(f"Error al insertar usuario en la base de datos: {e}")
        return False
