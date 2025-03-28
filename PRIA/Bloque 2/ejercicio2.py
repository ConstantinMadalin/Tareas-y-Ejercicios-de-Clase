import argparse

def celsius_a_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def main():
    parser = argparse.ArgumentParser(description="Conversor de temperatura")
    parser.add_argument("--temp", required=True, type=float, help="Valor de temperatura a convertir.")
    parser.add_argument("--scale", choices=["C", "F"], default="C", help="Escala de entrada (C o F). Por defecto: C.")

    args = parser.parse_args()

    if args.scale == "C":
        print(f"{args.temp}°C son {celsius_a_fahrenheit(args.temp):.2f}°F.")
    else:
        print(f"{args.temp}°F son {fahrenheit_a_celsius(args.temp):.2f}°C.")

if __name__ == "__main__":
    main()