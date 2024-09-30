#Crear el diccionario inicial
informacion_personal = {
    "nombre": "Ralph Aveiga",
    "edad": 40,
    "ciudad": "Santa Elena",
    "profesion": "Servidor publico"
}
#Acceder al valor de "ciudad" y modificarlo
informacion_personal["ciudad"] = "Salinas"
#Actualizar la clave de la profesión
informacion_personal["profesion"] = "Asistente administrativo"
#Verificar si la clave "telefono" existe y agregarla si no está
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "45116"
#Eliminar la clave "edad"
informacion_personal.pop("edad")
#Imprimir el diccionario final
print("Diccionario final:", informacion_personal)
# Imprimir cada clave y valor usando iteración
print("Diccionario final:")
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")
