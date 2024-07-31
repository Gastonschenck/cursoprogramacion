def leernombredesdeteclado (textoamostrar):
    nombreingresado=input(textoamostrar)
    return nombreingresado


def imprimirnombreyapellido ():
    nombre=leernombredesdeteclado("ingrese nombre: ")
    apellido=leernombredesdeteclado("ingrese apellido: ")
    print("su nombre completo es: ", nombre,"",apellido)

imprimirnombreyapellido()