#Practica: REGISTRO_ADQUIRIR_CONOCIMIENTO
#Alumno: IVAN_DOMINGUEZ
#Registro: 21310234
#Grupo: 7F1

import json  # Módulo para manejar archivos JSON
import os    # Módulo para manejar operaciones del sistema de archivos

# Ruta donde se almacenará la base de conocimiento
# Si el archivo no existe, se creará uno con el nombre "base_conocimiento.json"
ruta_base_conocimiento = "base_conocimiento.json"

# Función para cargar la base de conocimiento desde un archivo JSON
def cargar_base_conocimiento():
    # Verificamos si el archivo de conocimiento ya existe
    if os.path.exists(ruta_base_conocimiento):
        # Si existe, lo abrimos y cargamos los datos como un diccionario
        with open(ruta_base_conocimiento, "r") as archivo:
            return json.load(archivo)  # Cargamos el contenido del archivo JSON como diccionario
    else:
        # Si el archivo no existe, creamos una base de conocimiento inicial
        return {
            "Hola": "¡Hola! ¿Cómo estás?",
            "¿Cómo estás?": "Estoy bien, gracias por preguntar.",
            "¿De qué te gustaría hablar?": "Podemos hablar de cualquier cosa que quieras."
        }

# Función para guardar la base de conocimiento en un archivo JSON
def guardar_base_conocimiento(base_conocimiento):
    # Abrimos o creamos el archivo "base_conocimiento.json" en modo escritura
    with open(ruta_base_conocimiento, "w") as archivo:
        # Guardamos la base de conocimiento como un archivo JSON
        # `indent=4` formatea el archivo JSON con indentación para que sea más legible
        json.dump(base_conocimiento, archivo, indent=4)

# Función para buscar una respuesta en la base de conocimiento
def buscar_respuesta(pregunta, base_conocimiento):
    # Usamos el método get del diccionario para buscar la pregunta
    # Si no la encuentra, retorna `None`
    return base_conocimiento.get(pregunta, None)

# Función para adquirir un nuevo conocimiento y agregarlo a la base de datos
def adquirir_conocimiento(pregunta, respuesta, base_conocimiento):
    # Agregamos la nueva pregunta y respuesta al diccionario (base de conocimiento)
    base_conocimiento[pregunta] = respuesta
    # Guardamos la base de conocimiento actualizada en el archivo JSON
    guardar_base_conocimiento(base_conocimiento)
    print("¡Gracias! He aprendido algo nuevo.")  # Confirmación al usuario

# Función principal del chat interactivo
def chat():
    print("¡Bienvenido al chat!")
    
    # Cargamos la base de conocimiento desde el archivo JSON (o creamos una nueva si no existe)
    base_conocimiento = cargar_base_conocimiento()
    
    # Bucle infinito para mantener el chat activo hasta que el usuario lo cierre
    while True:
        # Pedimos al usuario que ingrese una pregunta
        pregunta_usuario = input("Tú: ")
        
        # Buscamos la respuesta en la base de conocimiento
        respuesta = buscar_respuesta(pregunta_usuario, base_conocimiento)
        
        # Si encontramos una respuesta (la pregunta ya está en la base)
        if respuesta:
            print(f"Sistema: {respuesta}")  # Mostramos la respuesta al usuario
        else:
            # Si no se encuentra la pregunta en la base, solicitamos información al usuario
            print("Sistema: No tengo una respuesta para eso. ¿Me podrías enseñar cuál sería una respuesta adecuada?")
            # El usuario nos proporciona la nueva respuesta
            nueva_respuesta = input("Tú: ")
            
            # Llamamos a la función para adquirir el nuevo conocimiento (agregarlo a la base)
            adquirir_conocimiento(pregunta_usuario, nueva_respuesta, base_conocimiento)

# Ejecutar el chat cuando se corre el programa
if __name__ == "__main__":
    chat()  # Llama a la función principal del chat

