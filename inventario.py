import sqlite3

# Conectar a la base de datos (se crea si no existe)
conn = sqlite3.connect("inventario.db")
cursor = conn.cursor()

# Crear la tabla productos si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        cantidad INTEGER NOT NULL
    )
''')

# Guardar cambios y cerrar conexión
conn.commit()
conn.close()

print("Base de datos y tabla 'productos' creadas correctamente.")