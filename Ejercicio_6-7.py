
# 6) Escribir un programa que pida al usuario un número, y:
# ● Si el valor ingresado es válido, lo imprima por pantalla.
# ● Si el valor ingresado no es numérico, imprima por pantalla “Debe ingresar un número válido”.
# ● Si contiene algún otro tipo de error, imprima por pantalla “Se produjo un error inesperado” junto con el error que surgió

numero_entrada = input("Ingrese un número: ")

try:
    numero = float(numero_entrada)
    # Se fuerza la entrada a la excepción con una división
    division =  100 / numero
except ValueError:
    print("Debe ingresar un número válido.")
except Exception as e:
    print(f"Se produjo un error inesperado: {e}")
else:
    print(f"Su número es: {numero}")
    
# 7) Repetir el ejercicio 6, pero añadiendo la posibilidad de que el usuario intente ingresar un
#    nuevo número luego de encontrar un error.

while True:
    numero_entrada = input("Ingrese un número: ")

    try:
        numero = float(numero_entrada)
        # Se fuerza la entrada a la excepción con una división
        division =  100 / numero
    except ValueError:
        print("Debe ingresar un número válido.")
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")
    else:
        print(f"Su número es: {numero}")
        print(f"Resultado de la división es: {division:.2f}")
        break