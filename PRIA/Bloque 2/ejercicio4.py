
import math
import argparse

def fibonacci_hasta_n(n):
    secuencia = [0, 1]
    while secuencia[-1] + secuencia[-2] <= n:
        secuencia.append(secuencia[-1] + secuencia[-2])
    return secuencia

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a  
        a, b = b, a + b  

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def menu():
    while True:
        print("\nSeleccione una opción:")
        print("1. Calcular la secuencia de Fibonacci hasta un número")
        print("2. Convertir temperatura de ºC a ºF")
        print("3. Convertir temperatura de ºF a ºC")
        print("4. Mostrar los primeros n números de Fibonacci")
        print("5. Salir")
        
        opcion = input("Ingrese el número de la opción: ")
        
        if opcion == "1":
            try:
                numero = int(input("Ingrese un número límite para la secuencia de Fibonacci: "))
                if numero < 0:
                    print("Por favor, ingrese un número positivo.")
                else:
                    print("Secuencia de Fibonacci hasta", numero, ":", fibonacci_hasta_n(numero))
            except ValueError:
                print("Por favor, ingrese un número válido.")
        
        elif opcion == "2":
            try:
                celsius = float(input("Ingrese la temperatura en ºC: "))
                print(f"{celsius} ºC equivalen a {celsius_a_fahrenheit(celsius):.2f} ºF")
            except ValueError:
                print("Por favor, ingrese un valor numérico válido.")
        
        elif opcion == "3":
            try:
                fahrenheit = float(input("Ingrese la temperatura en ºF: "))
                print(f"{fahrenheit} ºF equivalen a {fahrenheit_a_celsius(fahrenheit):.2f} ºC")
            except ValueError:
                print("Por favor, ingrese un valor numérico válido.")

        elif opcion == "4":
            try:
                n = int(input("Ingrese la cantidad de números de Fibonacci a mostrar: "))
                if n < 0:
                    print("Por favor, ingrese un número positivo.")
                else:
                    print(f"Los primeros {n} números de Fibonacci son:")
                    for num in fibonacci(n):
                        print(num)
            except ValueError:
                print("Por favor, ingrese un número válido.")
        
        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        
        else:
            print("Por favor, seleccione una opción válida.")

def main():
    parser = argparse.ArgumentParser(description="Conversor de temperatura y secuencia de Fibonacci")
    parser.add_argument("--temp", type=float, help="Valor de temperatura a convertir.")
    parser.add_argument("--scale", choices=["C", "F"], help="Escala de entrada (C o F).")
    parser.add_argument("--fibonacci", type=int, help="Número límite para calcular la secuencia de Fibonacci.")
    parser.add_argument("--first_n_fibonacci", type=int, help="Cantidad de números de Fibonacci a mostrar.")

    args = parser.parse_args()

    if args.temp is not None and args.scale:
        if args.scale == "C":
            print(f"{args.temp}°C son {celsius_a_fahrenheit(args.temp):.2f}°F.")
        elif args.scale == "F":
            print(f"{args.temp}°F son {fahrenheit_a_celsius(args.temp):.2f}°C.")

    if args.fibonacci is not None:
        if args.fibonacci < 0:
            print("Por favor, ingrese un número positivo para Fibonacci.")
        else:
            print("Secuencia de Fibonacci hasta", args.fibonacci, ":", fibonacci_hasta_n(args.fibonacci))

    if args.first_n_fibonacci is not None:
        if args.first_n_fibonacci < 0:
            print("Por favor, ingrese un número positivo para los primeros números de Fibonacci.")
        else:
            print(f"Los primeros {args.first_n_fibonacci} números de Fibonacci son:")
            for num in fibonacci(args.first_n_fibonacci):
                print(num)

    if args.temp is None and args.fibonacci is None and args.first_n_fibonacci is None:
        menu()

if __name__ == "__main__":
    main()