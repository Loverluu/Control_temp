def is_overheating(temp_c):

    if temp_c < 0:
        raise ValueError("Error de sensor: temperatura negativa")

    return temp_c > 80