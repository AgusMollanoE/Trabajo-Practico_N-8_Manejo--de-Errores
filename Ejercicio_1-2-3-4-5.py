import os

# Funciones para uso del sistema. Limpiar y pausar la terminal.
def limpiar_pantalla():
    os.system("cls")
    
def pausar():
    os.system("pause")

limpiar_pantalla()
print("-------------------------------------")
print("|      TRABAJO PRACTICO N° 8        |")
print("|        Manejo de Errores          |")
print("-------------------------------------")

while True:
    print("-------------------------------------")
    print("|      Seleccione una opción        |")
    print("-------------------------------------")
    print("| 1. Ejercicio N° 1                 |")
    print("| 2. Ejercicio N° 2                 |")
    print("| 3. Ejercicio N° 3                 |")
    print("| 4. Ejercicio N° 4                 |")
    print("| 5. Ejercicio N° 5                 |")
    print("| 0. Salir                          |")
    print("-------------------------------------")
    
    opcion = input("Ingrese opción: ")
    limpiar_pantalla()
    
    
    if opcion == "1":
        print("-------------------------------------")
        print("|          EJERCICIO N° 1           |")
        print("-------------------------------------")
        
        # Ejercicio 1
        #  1) Identifica los errores del código usando comentarios (#) en las líneas afectadas. Indica el tipo
        #    de error y una breve explicación de por qué ocurre.
        #    Ejemplo: c = a / b # Error: TypeError. 'b' es un string y no permite la división[cite: 14].
                
        # Ejemplo 1
        a = 10
        b = input("Introduce un número: ")
        result = a / b  # Error: TypeError. 'b' es una cadena (str) retornada por input() y no permite la división con un número entero.
        # Nota: Si el usuario ingresara '0' tras convertirlo a entero/flotante, también ocurriría un ZeroDivisionError.
        print(f"Resultado: {result}")

        # Ejemplo 2
        numbers = [1, 2, 3]
        print(numbers[5])  # Error: IndexError. El índice 5 está fuera de rango, ya que la lista contiene únicamente 3 elementos (índices 0, 1 y 2).

        pausar()
        limpiar_pantalla()
    
        
    elif opcion == "2":
        print("-------------------------------------")
        print("|          EJERCICIO N° 2           |")
        print("-------------------------------------")
        # Ejercicio 2
        # 2) Utilizando el código del ejercicio 1, arreglar los errores para que la ejecución del programa
        #   sea correcta sin necesidad de usar excepciones.
        
        print("\n---------------------------------------------------")
        print("------------------   Ejemplo 1   ------------------")
        print("---------------------------------------------------")
        a = 10
        b = int(input("Introduce un número: "))
        if b != 0:
            resultado = a/b
            print(f"Resultado: {resultado:.2f}")
        else:
            print("Error. No se puede dividir por 0.")
        
        print("\n---------------------------------------------------")
        print("------------------   Ejemplo 2   ------------------")
        print("---------------------------------------------------") 
                 
        numbers = [1, 2, 3]
        print(f"Se imprime el índice N° 1: {numbers[1]} de la siguiente lista: [1, 2, 3]\n") 
        
        pausar()
        limpiar_pantalla()

    elif opcion == "3":
        print("-------------------------------------")
        print("|          EJERCICIO N° 3           |")
        print("-------------------------------------")
        
        #3) Utilizando el código del ejercicio 1, mantener el código con los errores originales e incluir
        #  bloques try-except para que la ejecución del programa no se frene al encontrar los errores.
        
        a = 10
        b = input("Introduce un número: ")
        try:
            resultado = a / b
            print(f"Resultado: {result}")
        
        except:
            print("\n---------------------------------------------------")
            print("------------------   Ejemplo 1   ------------------")
            print("---------------------------------------------------")
            print("ERROR: Ocurrió un problema en la división")
            
        #Ejemplo 2
        numbers = [1, 2, 3]
        try:
            print(numbers[5])
            
        except:
            print("\n---------------------------------------------------")
            print("------------------   Ejemplo 2   ------------------")
            print("---------------------------------------------------")
            # Se muestran estos print() para que se pueda visualizar mejor el error en consola y se observe el error
            print("numbers = [1, 2, 3]")
            print("print(numbers[5])")
            print("\nERROR: El índice especificado está fuera del rango de la lista.\n")
        
        pausar()
        limpiar_pantalla()
        
    elif opcion == "4":
        print("-------------------------------------")
        print("|          EJERCICIO N° 4           |")
        print("-------------------------------------")
        
        #4) Repetir el ejercicio 3, pero usando excepciones múltiples que hagan alusión a lostipos de
        #  errores detectados.
        
        a = 10
        b = input("Introduce un número: ")
        try:
            resultado = a / b
            print(f"Resultado: {result}")
                
        except TypeError:
            print("\n---------------------------------------------------")
            print("------------------   Ejemplo 1   ------------------")
            print("---------------------------------------------------")
            print("ERROR: Ocurrió un problema en la división")
        except ZeroDivisionError:
            print("ERROR: No se puede dividir por 0.")
                    
        #Ejemplo 2
        numbers = [1, 2, 3]
        try:
            print(numbers[5])
                    
        except IndexError:
            print("\n---------------------------------------------------")
            print("------------------   Ejemplo 2   ------------------")
            print("---------------------------------------------------")
            print("numbers = [1, 2, 3]")
            print("print(numbers[5])")
            print("\nERROR: El índice especificado está fuera del rango de la lista.\n")
        
        
        pausar()
        limpiar_pantalla()
        
    elif opcion == "5":
        print("-------------------------------------")
        print("|          EJERCICIO N° 5           |")
        print("-------------------------------------")
        #Ejercicio 5
        #5) Repetir el ejercicio 4, pero esta vezincluyendo bloques else y finally.
        
        # Ejercicio 5

        # Ejemplo 1
        a = 10
        b = input("Introduce un número: ")

        try:
            result = a / b
        except TypeError:
            print("Error: No se puede dividir un entero por una cadena de texto (str).")
        except ZeroDivisionError:
            print("Error: No se puede dividir por cero.")
        else:
            print(f"Resultado: {result}")
        finally:
            print("Operación del Ejemplo 1 finalizada.")

        # Ejemplo 2
        numbers = [1, 2, 3]

        try:
            print(numbers[5])
        except IndexError:
            print("Error: El índice especificado está fuera del rango de la lista.")
        else:
            print("Acceso a la lista realizado con éxito.")
        finally:
            print("Operación del Ejemplo 2 finalizada.")
            
            
        pausar()
        limpiar_pantalla()

    elif opcion == "0":
        print("-------------------------------------")
        print("| ¡Hasta luego!                     |")
        print("-------------------------------------\n")
        break
    
    else:
        print("Opción inválida. Ingrese una opción válida.\n")
        pausar()
        limpiar_pantalla()