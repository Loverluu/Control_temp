from temperature import esta_en_alarma

try:
    temp = float(input("Ingrese temperatura: "))

    if esta_en_alarma(temp):
        print("⚠️ ALARMA: Temperatura alta")
    else:
        print("✅ Temperatura normal")

except ValueError:
    print("❌ Error: ingreso inválido")