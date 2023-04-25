edad = int(input("Proporciona tu edad:"))

if 0 <= edad <= 10:
    print("La infancia es inceríble...")
elif 10 < edad <= 20:
    print("Muchos cambios y mucho estudio...")
elif 20 < edad <= 30:
    print("Amor y comenza el trabajo...")
else:
    print("Etapa de vida no reconocida")