#---------- Ejercicios de Listas y Diccionarios ---------
#Le pedí a la IA una lista de ejercicios para reforzar los conceptros de listas y diccionarios
#pues ha mencionado que son de mucha utilidad más adelante.
"""
EJERCICIOS:
--- Listas ---
1. Crea una lista vacía de frutas. Agrega tres con append.
   Agrega una más al inicio con insert. Imprime la lista.
2. Tienes otra lista con ["uva", "kiwi"]. Únela a la primera con extend.
   Después invierte el orden con reverse() e imprímela.
3. Quita la última fruta con pop() y guárdala en una variable.
   Imprime la fruta que quitaste y cómo quedó la lista.
4. Pide números al usuario hasta que escriba 0, guárdalos en una lista
   (con append) y al final muestra la lista, su suma y el mayor
   (puedes usar sum() y max()).

--- Diccionarios ---
5. Crea un diccionario con 3 alumnos y su calificación.
   Imprime la calificación de uno con [] y de otro con get.
6. Pide un nombre. Con get, muestra su calificación o "No existe"
   si no está en el diccionario.
7. Agrega un alumno nuevo y cambia la calificación de otro
   usando update.
8. Recorre el diccionario con un for e imprime "nombre: calificación".
   Después imprime solo los nombres (keys) y solo las calificaciones (values).
9. Quita un alumno con pop y muestra qué calificación tenía.

--- Reto final (junta todo) ---
10. Una lista de la compra con menú: 1) Agregar, 2) Quitar,
    3) Ver lista, 4) Salir. Se repite con while True hasta elegir 4.
    (Pista: es el menú que ya hiciste, pero ahora cada opción
    modifica una lista con append, remove o pop.)
"""

#Ejercicios 1-3:
def main1():
    frutas = []
    frutas.append("limon")
    frutas.append("manzana")
    frutas.append("sandia")
    frutas.insert(0,"melon")
    print(frutas)
    frutas2=["lima","pepino"]
    frutas.extend(frutas2)
    frutas.reverse()
    print(f"Lista de frutas: \n{frutas}")
    variable = frutas.pop(5)
    print(f"fruta eliminada: {variable}")
    print(f"Lista de frutas sin {variable}: {frutas}")
#main1()

#Ejercicio 4:
def main2():
    
main2()