# Calculadora de impuestos para la SUNAT
# Variables globales
UIT = 4200

# Se obtienen los datos del usuario
print("Bienvenido al calculador de impuesto de la SUNAT. Si usted se encuentra en planilla, por favor continue con el formulario:")
print("1. Cual es el nombre completo de su empleado?")
nombre = input()

print("2. De cuanto es su remuneracion mensual?")
remuneracion_mensual = input()
if isinstance(remuneracion_mensual,int) or isinstance(remuneracion_mensual,float):
    if remuneracion_mensual < 0:
        print("No puede ingresar un valor negativo")
else:
    print("Debe ingresar un valor numerico")

print("3. Cuantos meses le faltan para terminar el ejercicio gravable (incluido el mes de la retencion)?")
meses_restantes = input()
if isinstance(meses_restantes,int) or isinstance(meses_restantes,float):
    if meses_restantes < 0:
        print("No puede ingresar un valor negativo")
else:
    print("Debe ingresar un valor numerico")

print("4. Cual es su monto obtenido por participación en las utilidades, gratificaciones o bonificaciones extraordinarias, o cualquier otro concepto extraordinario?")
monto_adicional = input()
if isinstance(monto_adicional,int) or isinstance(monto_adicional,float):
    if monto_adicional < 0:
        print("No puede ingresar un valor negativo")
else:
    print("Debe ingresar un valor numerico")

print("5. Si ha tenido ingresos adicionales gravados con rentas de quinta categoria, de que monto han sido (acumulado)?")
adicionales_gravados = input()
if isinstance(adicionales_gravados,int) or isinstance(adicionales_gravados,float):
    if adicionales_gravados < 0:
        print("No puede ingresar un valor negativo")
else:
    print("Debe ingresar un valor numerico")

print("6. Si ha recibido ingresos extraordinarios, de cuanto han sido? (Separe los valores con espacios)")
print("Array: [Enero, febrero, marzo; Abril; Mayo, junio, julio; Agosto; Septiembre, octubre, noviembre; Diciembre]")
monto_array = input()
monto_extraordinario = monto_array.split()

gratificaciones_ordinarias = 2*float(remuneracion_mensual)

# PASO 1: Se proyectan los ingresos gravados que percibirá en todo el año.
print(f"El resumen de impuestos a la renta de quinta categoria de {nombre} es: ")
remuneracion_bruta_anual = (float(remuneracion_mensual) * float(meses_restantes)) + float(gratificaciones_ordinarias) + float(monto_adicional)
print(f"Su remuneracion bruta anual (sin adicionales gravados) es de: {remuneracion_bruta_anual}")
remuneracion_bruta_anual += float(adicionales_gravados)
print(f"Su remuneracion bruta anual (con adicionales gravados) es de: {remuneracion_bruta_anual}")

# PASO 2: Se realiza la deducción de 7 UIT.
if(remuneracion_bruta_anual > (7*UIT)):
    remuneracion_neta_anual = remuneracion_bruta_anual - 7*UIT
    print(f"Su remuneracion neta anual es de: {remuneracion_neta_anual}")

    # PASO 3: Cálculo del impuesto anual proyectado.
    if(remuneracion_bruta_anual <= (5*UIT)):
        impuesto_anual = remuneracion_neta_anual*0.08
    elif((5*UIT) < remuneracion_bruta_anual <= (20*UIT)):
        impuesto_anual = remuneracion_neta_anual*0.14
    elif((20*UIT) < remuneracion_bruta_anual <= (35*UIT)):
        impuesto_anual = remuneracion_neta_anual*0.17
    elif((35*UIT) < remuneracion_bruta_anual <= (45*UIT)):
        impuesto_anual = remuneracion_neta_anual*0.2
    else:
        impuesto_anual = remuneracion_neta_anual*0.3

    print(f"Su impuesto anual proyectado es de: {impuesto_anual}")

    # PASO 4: Monto de la retención.
    # Se inicializa el array
    monto_retencion_mensual = [0, 0, 0, 0, 0, 0] 
    retencion_total_mensual = [0, 0, 0, 0, 0, 0]
    factor_division = [12, 9, 8, 5, 4, 1]
    monto_retencion_efectuada = 0

    for mes in range(6):
        monto_retencion_mensual[mes] = (impuesto_anual - monto_retencion_efectuada) / factor_division[mes]
        print(monto_retencion_mensual[mes])
        monto_retencion_efectuada += monto_retencion_mensual[mes]
        
        # Cálculo adicional SOLO para los meses en que el trabajador ha recibido pagos distintos a las remuneraciones y gratificaciones ordinarias.
        remuneracion_bruta_adicional = remuneracion_bruta_anual + float(monto_extraordinario[mes])
        remuneracion_neta_adicional = remuneracion_bruta_adicional - 7*UIT

        if(remuneracion_bruta_adicional <= (5*UIT)):
            retencion_adicional = (remuneracion_neta_adicional*0.08) - impuesto_anual
        elif((5*UIT) < remuneracion_bruta_adicional <= (20*UIT)):
            retencion_adicional = (remuneracion_neta_adicional*0.14) - impuesto_anual
        elif((20*UIT) < remuneracion_bruta_adicional <= (35*UIT)):
            retencion_adicional = (remuneracion_neta_adicional*0.17) - impuesto_anual
        elif((35*UIT) < remuneracion_bruta_adicional <= (45*UIT)):
            retencion_adicional = (remuneracion_neta_adicional*0.2) - impuesto_anual
        else:
            retencion_adicional = (remuneracion_neta_adicional*0.3) - impuesto_anual

        retencion_total_mensual[mes] = monto_retencion_mensual[mes] + retencion_adicional

    print(f"El cronograma de pagos es el siguiente:")
    print(f"Su monto de retencion para el mes de Enero es de: {retencion_total_mensual[0]}")
    print(f"Su monto de retencion para el mes de Febrero es de: {retencion_total_mensual[0]}")
    print(f"Su monto de retencion para el mes de Marzo es de: {retencion_total_mensual[0]}")
    print(f"Su monto de retencion para el mes de Abril es de: {retencion_total_mensual[1]}")
    print(f"Su monto de retencion para el mes de Mayo es de: {retencion_total_mensual[2]}")
    print(f"Su monto de retencion para el mes de Junio es de: {retencion_total_mensual[2]}")
    print(f"Su monto de retencion para el mes de Julio es de: {retencion_total_mensual[2]}")
    print(f"Su monto de retencion para el mes de Agosto es de: {retencion_total_mensual[3]}")
    print(f"Su monto de retencion para el mes de Septiembre es de: {retencion_total_mensual[4]}")
    print(f"Su monto de retencion para el mes de Octubre es de: {retencion_total_mensual[4]}")
    print(f"Su monto de retencion para el mes de Noviembre es de: {retencion_total_mensual[4]}")
    print(f"Su monto de retencion para el mes de Diciembre es de: {retencion_total_mensual[5]}")
else:
    print("A usted no se le aplican retenciones debido a que su remuneracion bruta anual es menor a 7 UIT.")

print("Gracias por usar la calculadora de impuesto de la SUNAT!")
