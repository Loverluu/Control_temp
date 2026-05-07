from temperature import is_overheating

try:
    temp = float(input("Ingrese temperatura: "))

    if is_overheating(temp):
        print("ALARMA: temperatura alta")
    else:
        print("Temperatura normal")

except ValueError as error:
    print(f"Error: {error}")
