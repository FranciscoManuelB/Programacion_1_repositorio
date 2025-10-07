def cuota_interes(interes, monto, anios):
    interes_mensual = (interes+1) / (12*anios) * monto
    num_cuotas = anios * 12
    cuota = (monto / (anios * 12))
    cuota_mensual = cuota + interes_mensual
    return interes_mensual, cuota_mensual
print(cuota_interes(0.02, 10000, 1))