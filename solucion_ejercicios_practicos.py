# Ejercicios Prácticos: Expresiones Aritméticas

#- Resuelve los ejercicios en orden
#- Intenta predecir el resultado antes de ejecutar el código
#- Verifica tus respuestas con Python
#- Si te equivocas, analiza por qué


## 🟢 NIVEL 1: Básico (Precedencia Simple)

### Ejercicio 1.1: Predice el Resultado

print(5 + 3 * 2)

#**Tu predicción**: 11
#**Resultado real**: 11 
#**Explicación**: Primero se multiplica el 3 por 2 lo que da 6, luego se suma el 5 y da 11.

#----------------------------------------------------------------------------------------------------------------------------------

### Ejercicio 1.2: Paréntesis

print((5 + 3) * 2)

#**Tu predicción**: 16
#**Resultado real**: 16
#**Explicación**: Primero se suma lo de adentro del parentesis, osea el 5+3, que da 8, luego se multiplica por 2, que da 16.

#----------------------------------------------------------------------------------------------------------------------------------

### Ejercicio 1.3: División

print(10 / 2)
print(10 // 2)
print(10 % 2)

#**Tu predicción**: 5, 5, 5.0
#**Resultado real**: 5.0, 5, 0
#**Explicación**: Yo pensaba que el simbolo (/) solo afectaba cuando una division si tenia decimales, pero al parecer también afecta
#a divisiones enteras dejandolo en float, el simbolo(//) efectivamente lo deja en int y el simbolo (%) pensaba que siempre lo dejaba
#en float, pero resulta ser el resto o también dicho como el residuo.

#----------------------------------------------------------------------------------------------------------------------------------

### Ejercicio 1.4: Potencia

print(2 ** 3)
print(2 ^ 3)

#**Tu predicción**: 8, 1
#**Resultado real**: 8, 1
#**Explicación**: El primero es el 2 con exponente 3, osea, 2x2x2. El segundo es el XOR bit a bit, basicamente 2 (que en bits es 10)
#menos 3 (que en bits es 11) lo que da 1.

#----------------------------------------------------------------------------------------------------------------------------------

### Ejercicio 1.5: Negación

print(5 - -3)
print(-5 * -3)

#**Tu predicción**: 8, 15
#**Resultado real**: 8, 15
#**Explicación**: El primer ejercicio es la resta de 5- (-3), cuando hay dos menos se suman y queda como una suma normal. En el
#segundo ejercicio es una multiplicacion y al igual que cuando hay dos restas seguidas, sí se multiplican dos numeros con simbolo
#negativo, queda en positivo, por lo que -5 * -3 da 15.

#----------------------------------------------------------------------------------------------------------------------------------

## 🟡 NIVEL 2: Intermedio (Expresiones Complejas)

### Ejercicio 2.1: Múltiples Operadores

print(2 + 3 * 4 - 5)

#**Tu predicción**: 9
#**Resultado real**: 9
#**Explicación**: Primero se resuelve la multiplicación, osea, 3*4=12, y ya luego la suma +2 y la resta -5 que no importa en que orden
#se resuelva, lo que da 9.

#----------------------------------------------------------------------------------------------------------------------------------

### Ejercicio 2.2: División y Multiplicación

print(20 / 4 * 2)
print(20 / (4 * 2))

#**Tu predicción**: 10.0, 2.5
#**Resultado real**: 10.0, 2.5
#**Explicación**: En el primer ejercicio la division y la multiplicación tienen la misma importancia para ser resuelto en orden,
#por lo que se resuelve de izquierda a derecha, lo que da 20/4=5.0 y luego 5*2=10.0 (teniendo en cuenta el float). En el 
#segundo ejercicio se resuelve primero lo que esta dentro del parentesis, osea, 4*2=8, luego se resuelve la divisio, 20/8=2.5.

#----------------------------------------------------------------------------------------------------------------------------------

### Ejercicio 2.3: Módulo en Expresión

print(17 % 5 + 2 * 3)

#**Tu predicción**: 8
#**Resultado real**: 8
#**Explicación**: Primero el 17%5=2, luego, 2*3=6 y luego se suma el 2+6=8.

#----------------------------------------------------------------------------------------------------------------------------------

### Ejercicio 2.4: Potencias Anidadas

print(2 ** 3 ** 2)
print((2 ** 3) ** 2)

#**Tu predicción**: 512, 64
#**Resultado real**: 512, 64
#**Explicación**: En el primer ejercicio se resuelve desde los exponentes, osea de derecha a izquierda, 3**2=3x3=9,
#luego 2**9=(nueve veces 2)=512. En el segundo ejercicio se resuelve primero lo de dentro del parentesis, osea,2**3=2x2x2=8 y luego
#8**2=8x8=64.

#----------------------------------------------------------------------------------------------------------------------------------

### Ejercicio 2.5: Expresión Compleja

print(10 + 5 * 2 - 8 / 4 + 3)

#**Tu predicción**: 21.0
#**Resultado real**: 21.0
#**Explicación**: De izquierda a derecha según la importancia, primero 5*2=10, luego -8/4=-2.0(con el float), por último todo lo demás,
#10+10-2.0+3=21.0.

#----------------------------------------------------------------------------------------------------------------------------------

## 🔴 NIVEL 3: Avanzado (Problemas del Mundo Real)

### Ejercicio 3.1: Cálculo de Impuestos

# Calcula el total con impuesto del 15% sobre una compra de $100.

price = 100
tax_rate = 0.15

#Resultado

total = price * (1 + tax_rate)

#----------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 3.2: Conersión de Temperatura

# Convierte 25°C a Fahrenheit usando la fórmula: F = (C × 9/5) + 32

celsius = 25

#Resultado:

Fahrenheit = (celsius * 9 / 5) + 32

#----------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 3.3: Promedio de Calificaciones

# Calcula el promedio de 3 calificaciones: 85, 90, 78

grade1 = 85
grade2 = 90
grade3 = 78

#Resultado

average = (grade1 + grade2 + grade3) / 3

#----------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 3.4: Dividir Cuenta

# 4 amigos van a cenar. La cuenta es $127.50. Calcula cuánto paga cada uno.

total_bill = 127.50
num_people = 4

# Resultado:

per_person = total_bill / num_people

#----------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 3.5: Tiempo Restante
# Tienes 125 minutos. ¿Cuántas horas y minutos son?

total_minutes = 125

#Resultado
#Horas
hours = total_minutes // 60

#Minutos
minutes = total_minutes % 60

#----------------------------------------------------------------------------------------------------------------------------------

## 🎯Proyecto Final: Calculadora de Expresiones
### Descripción
#Crea un programa que:
#1. Solicite una expresión al usuario
#2. Evalúe la expresión
#3. Muestre el resultado
#4. Maneje errores básicos

# Tu código aquí

expression = input("Ingresa una expresión: ")

# Evaluar y mostrar resultado
# Manejar división por cero
# Manejar expresiones inválidas

def calcular_expresion():
    while True:
        expresion = input("Escribe una operación (o 'fin' para salir): ").strip()
        
        if expresion.lower() == "fin":
            print("\nPrograma finalizado. ¡Gracias por usar la calculadora!")
            break

        try:
            valor = eval(expresion)
            print(f" Resultado: {valor}  ({type(valor).__name__})\n")
        except ZeroDivisionError:
            print(" No se puede dividir entre cero.\n")
        except Exception:
            print(" La expresión ingresada no es válida.\n")

def mostrar_menu():
    print("====== CALCULADORA ======")
    print("Operaciones válidas: +, -, *, /, //, %, **")
    print("Escribe 'fin' para cerrar el programa.\n")

if __name__ == "__main__":
    mostrar_menu()
    calcular_expresion()


# 📊Ejercicios de Debugging

# Debug 1: Encuentra el error

# Este código debería calcular el promedio

a = 10
b = 20
c = 30
average = a + b + c / 3

#¿Qué está mal?:
# Los 3 valores estan mal porque tendrían que estar entre paréntesis, para que solo divida la c por 3

print(f"Promedio: {average}")

# Debug 2: Encuentra el error

# Calcular 20% de descuento sobre $50
price = 50
discount = 20
final = price - discount * price
print(f"Precio final: ${final}")

#¿Qué está mal?:
# El error esta en la multiplicación, ya que se está multiplicando el descuento por el precio "20 * 50 = 1000"

