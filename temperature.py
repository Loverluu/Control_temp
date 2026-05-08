def esta_en_alarma(temp_c):
    if temp_c < 0:
        raise ValueError("Error de lectura")

    return temp_c > 80