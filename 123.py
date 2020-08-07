moneda = int(input ('ingrese pais:{pais} '))
if pais == COLOMBIA:
    cantidad = int(input ('monto: '))
    total = cantidad * 0.00027
elif pais == EEUU:
    cantidad = int(input ('monto: '))
    total = cantidad * 1.19
else pais == PERU:
    cantidad = int(input ('monto: '))
    total = cantidad * 0.56

print moneda