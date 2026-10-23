"""
u can use f strings to write text and variables in the same print
"""
#for example:
name = input("what´s your name:")
print (f"Hello, {name}", end="\nsee?") 
#tambien puedes sumar numeros en los corchetes
print(f"la suma de 2+2 es: {2+2}")
#estos son "methods", son subrutinas que permiten modificar la logica de una fuincion
#a diferencia de un parametro que es opcional y se trata de acciones que peudes modificar
#DENTRO DE LA PROPIA FUNCION
#los methods parece que se modifican desde afuera
name = input("escribe tu nombre")
print(name).strip().title()
#strip es una "subfuncion" que quita lo que esta dentro del parentresis (espacio)
#de la ixquierda y derecha de lo q ingreso el usuario
#title pone en capital letter every firts letter of every word the user writes
#this are methods u use for every object (type string), like input, it gives output (string)
#so u can use it to input too, but for floats no
#puedes usarlo en diferentes lineas tambien
name=name.strip()
name=name.title()
#si se pone longer u can use methods separete
