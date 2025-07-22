# progrma que me permite mostrar todas las tablas de multiplicar

# con el primer bucle mostramos el nombre de la tabla
for tabla in range(1, 11):
    print(f"\nTabla # {tabla}")
    # con el segundo hacemos la operacion de esa tabla
    for num in range(1, 11):
        resultado = tabla * num
        print(f"{tabla} x {num} = {resultado}")  # Mostramos el resultado en pantalla
