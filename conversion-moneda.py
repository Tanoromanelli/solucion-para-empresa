

    # Paso 1: Definir el valor actual
tipo_cambio_eur_a_mxn = 23.70
tipo_cambio_usd_a_mxn = 20.75

    # Paso 2: Solicitar al usuario el tipo de conversión (eu a mxn o dol a mxn)
tipo_conversion = input("Ingrese la moneda origen a convertir (EUR/USD): ")

    # Paso 3: Solicitar el monto a ocnvertir
monto_a_convertir = float(input(("Ingrese el monto a convertir: ")))

    # Paso 4: Realizar la conversión utilizando TC corresponciente

if tipo_conversion.upper() == "EUR":
    resultado = monto_a_convertir * tipo_cambio_eur_a_mxn 
    print("El resultado de la conversion de EUR a MXN es: ", resultado) 
elif tipo_conversion == "USD":
    resultado = monto_a_convertir + tipo_cambio_usd_a_mxn
    print("El resultado de la conversion de USD a MXN es: ", resultado) 
else:
    print("No está disponible")