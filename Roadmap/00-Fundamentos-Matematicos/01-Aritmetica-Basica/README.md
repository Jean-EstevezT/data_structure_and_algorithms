# 🔢 Aritmética Básica

## 📋 Tabla de Contenidos

1. [Introducción](#introducción)
2. [Operaciones Fundamentales](#operaciones-fundamentales)
3. [Divisibilidad](#divisibilidad)
4. [El Operador Resto (Módulo)](#el-operador-resto-módulo)
5. [Propiedades de las Operaciones](#propiedades-de-las-operaciones)
6. [Representación de Números](#representación-de-números)
7. [Overflow y Underflow](#overflow-y-underflow)
8. [Aplicaciones en Algoritmos](#aplicaciones-en-algoritmos)
9. [Ejercicios Prácticos](#ejercicios-prácticos)

---

## Introducción

La aritmética básica es el fundamento de todo algoritmo. Comprender cómo funcionan las operaciones numéricas, la divisibilidad y el operador módulo es esencial para resolver problemas de programación competitiva y entrevistas técnicas.

### ¿Por qué es importante?

- **Análisis de complejidad:** Entender operaciones O(1)
- **Manipulación de índices:** Arrays, matrices, búsqueda binaria
- **Criptografía básica:** Hash functions, checksums
- **Optimización:** Evitar operaciones costosas

---

## Operaciones Fundamentales

### Las 4 Operaciones Básicas

| Operación | Símbolo | Python | Ejemplo | Resultado |
|-----------|---------|--------|---------|-----------|
| Suma | + | `a + b` | `5 + 3` | `8` |
| Resta | - | `a - b` | `5 - 3` | `2` |
| Multiplicación | × | `a * b` | `5 * 3` | `15` |
| División | ÷ | `a / b` | `5 / 3` | `1.666...` |

### División Entera vs División Real

```python
# División real (float)
print(7 / 3)    # 2.3333...

# División entera (floor division)
print(7 // 3)   # 2

# ⚠️ Cuidado con números negativos
print(-7 // 3)  # -3 (no -2!)
# Python usa floor division, que redondea hacia -∞
```

### Potenciación

```python
# Exponenciación básica
print(2 ** 10)      # 1024

# Exponenciación modular (muy importante en competencias)
print(pow(2, 10, 1000))  # 24 (equivale a 2^10 % 1000)

# pow(base, exp, mod) es O(log exp) - ¡muy eficiente!
```

### Raíz Cuadrada

```python
import math

# Raíz cuadrada
print(math.sqrt(16))      # 4.0
print(math.isqrt(16))     # 4 (entero)

# Para verificar si es cuadrado perfecto
def es_cuadrado_perfecto(n):
    raiz = math.isqrt(n)
    return raiz * raiz == n

print(es_cuadrado_perfecto(16))  # True
print(es_cuadrado_perfecto(15))  # False
```

---

## Divisibilidad

### Definición

Un número `a` es **divisible** por `b` si existe un entero `k` tal que `a = b × k`.

Notación: `b | a` significa "b divide a a"

### Verificar Divisibilidad

```python
def es_divisible(a, b):
    """Verifica si a es divisible por b"""
    return a % b == 0

# Ejemplos
print(es_divisible(12, 3))   # True (12 = 3 × 4)
print(es_divisible(12, 5))   # False
print(es_divisible(0, 5))    # True (0 es divisible por cualquier número)
```

### Reglas de Divisibilidad

| Divisor | Regla | Ejemplo |
|---------|-------|---------|
| **2** | Último dígito es par (0,2,4,6,8) | 124 ✓ |
| **3** | Suma de dígitos divisible por 3 | 123 → 1+2+3=6 ✓ |
| **4** | Últimos 2 dígitos divisibles por 4 | 316 → 16÷4=4 ✓ |
| **5** | Último dígito es 0 o 5 | 125 ✓ |
| **6** | Divisible por 2 Y por 3 | 126 ✓ |
| **8** | Últimos 3 dígitos divisibles por 8 | 1016 → 16÷8=2 ✓ |
| **9** | Suma de dígitos divisible por 9 | 729 → 7+2+9=18 ✓ |
| **10** | Último dígito es 0 | 120 ✓ |
| **11** | Diferencia alternada de dígitos div. por 11 | 121 → 1-2+1=0 ✓ |

### Implementación de Reglas

```python
def suma_digitos(n):
    """Suma todos los dígitos de n"""
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

def divisible_por_3(n):
    return suma_digitos(n) % 3 == 0

def divisible_por_9(n):
    return suma_digitos(n) % 9 == 0

# Alternativa más pythonica
def suma_digitos_v2(n):
    return sum(int(d) for d in str(abs(n)))
```

### Divisores de un Número

```python
def obtener_divisores(n):
    """Obtiene todos los divisores de n en O(√n)"""
    divisores = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisores.append(i)
            if i != n // i:
                divisores.append(n // i)
        i += 1
    return sorted(divisores)

print(obtener_divisores(12))   # [1, 2, 3, 4, 6, 12]
print(obtener_divisores(100))  # [1, 2, 4, 5, 10, 20, 25, 50, 100]
```

### Contar Divisores

```python
def contar_divisores(n):
    """Cuenta los divisores de n en O(√n)"""
    count = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
        i += 1
    return count

print(contar_divisores(12))   # 6
print(contar_divisores(100))  # 9
```

---

## El Operador Resto (Módulo)

### Definición

El operador módulo `%` devuelve el **resto** de la división entera.

```
a = (a // b) * b + (a % b)
```

### Sintaxis

```python
# Básico
print(17 % 5)    # 2 (porque 17 = 5*3 + 2)
print(10 % 3)    # 1
print(9 % 3)     # 0

# Con negativos (¡cuidado!)
print(-17 % 5)   # 3 en Python (no -2)
# Python garantiza: 0 <= a % b < b (para b > 0)
```

### Propiedades del Módulo

```python
# 1. (a + b) % m = ((a % m) + (b % m)) % m
a, b, m = 17, 23, 10
print((a + b) % m)                    # 0
print(((a % m) + (b % m)) % m)        # 0 ✓

# 2. (a - b) % m = ((a % m) - (b % m) + m) % m
print((a - b) % m)                    # 4
print(((a % m) - (b % m) + m) % m)    # 4 ✓

# 3. (a * b) % m = ((a % m) * (b % m)) % m
print((a * b) % m)                    # 1
print(((a % m) * (b % m)) % m)        # 1 ✓

# 4. (a ^ n) % m → usar pow(a, n, m) para eficiencia O(log n)
print(pow(2, 1000, 1000000007))       # Resultado pequeño, cálculo eficiente
```

### Aplicaciones Comunes

```python
# 1. Verificar paridad
def es_par(n):
    return n % 2 == 0

# 2. Obtener último dígito
def ultimo_digito(n):
    return n % 10

# 3. Obtener últimos k dígitos
def ultimos_k_digitos(n, k):
    return n % (10 ** k)

# 4. Wrap-around (índices circulares)
def indice_circular(i, longitud):
    return i % longitud

lista = [1, 2, 3, 4, 5]
for i in range(10):
    print(lista[i % len(lista)], end=" ")  # 1 2 3 4 5 1 2 3 4 5

# 5. Determinar día de la semana
dias = ["Lun", "Mar", "Mie", "Jue", "Vie", "Sab", "Dom"]
def dia_despues_de_n_dias(dia_actual, n):
    return dias[(dias.index(dia_actual) + n) % 7]
```

---

## Propiedades de las Operaciones

### Propiedades de la Suma

| Propiedad | Descripción | Ejemplo |
|-----------|-------------|---------|
| **Conmutativa** | a + b = b + a | 3 + 5 = 5 + 3 |
| **Asociativa** | (a + b) + c = a + (b + c) | (2+3)+4 = 2+(3+4) |
| **Elemento neutro** | a + 0 = a | 7 + 0 = 7 |
| **Elemento opuesto** | a + (-a) = 0 | 5 + (-5) = 0 |

### Propiedades de la Multiplicación

| Propiedad | Descripción | Ejemplo |
|-----------|-------------|---------|
| **Conmutativa** | a × b = b × a | 3 × 5 = 5 × 3 |
| **Asociativa** | (a × b) × c = a × (b × c) | (2×3)×4 = 2×(3×4) |
| **Elemento neutro** | a × 1 = a | 7 × 1 = 7 |
| **Elemento absorbente** | a × 0 = 0 | 7 × 0 = 0 |
| **Distributiva** | a × (b + c) = a×b + a×c | 2×(3+4) = 2×3 + 2×4 |

### Propiedades Útiles en Algoritmos

```python
# 1. Distributiva para simplificar
# En vez de: (a*c + b*c), usar: (a + b) * c
resultado = (5 + 3) * 2  # Más eficiente: 1 multiplicación

# 2. Para evitar overflow en suma
# En vez de: (a + b) / 2, usar: a + (b - a) / 2
def punto_medio_seguro(a, b):
    return a + (b - a) // 2

# 3. Intercambio sin variable temporal (XOR)
a, b = 5, 3
a = a ^ b
b = a ^ b
a = a ^ b
print(a, b)  # 3, 5
```

---

## Representación de Números

### Sistemas Numéricos

| Base | Nombre | Prefijo Python | Ejemplo |
|------|--------|----------------|---------|
| 2 | Binario | `0b` | `0b1010` = 10 |
| 8 | Octal | `0o` | `0o12` = 10 |
| 10 | Decimal | (ninguno) | `10` |
| 16 | Hexadecimal | `0x` | `0xA` = 10 |

### Conversiones

```python
n = 42

# Decimal a otras bases
print(bin(n))   # '0b101010'
print(oct(n))   # '0o52'
print(hex(n))   # '0x2a'

# Otras bases a decimal
print(int('101010', 2))   # 42
print(int('52', 8))       # 42
print(int('2a', 16))      # 42

# Número de bits necesarios
print(n.bit_length())     # 6 (porque 42 = 101010 en binario)
```

### Números Negativos (Complemento a 2)

```python
# En Python los enteros tienen precisión arbitraria
# Pero en otros lenguajes y a nivel de bits:

# Complemento a 2 para -5 en 8 bits:
# 5 = 00000101
# Invertir: 11111010
# Sumar 1: 11111011 = -5

# Con Python y bit_length negativo
n = -5
print(bin(n))  # '-0b101' (Python muestra el signo)
```

---

## Overflow y Underflow

### ¿Qué son?

- **Overflow:** Cuando el resultado excede el valor máximo representable
- **Underflow:** Cuando el resultado es menor que el valor mínimo representable

### En Python

```python
# Python tiene enteros de precisión arbitraria - ¡no hay overflow!
n = 10 ** 1000
print(len(str(n)))  # 1001 dígitos, sin problema

# Pero si trabajas con otros lenguajes o límites específicos:
# int32: -2,147,483,648 a 2,147,483,647
# int64: -9,223,372,036,854,775,808 a 9,223,372,036,854,775,807
```

### Prevenir Overflow

```python
# 1. Usar módulo para mantener números pequeños
MOD = 10**9 + 7

def multiplicar_seguro(a, b):
    return (a % MOD) * (b % MOD) % MOD

# 2. Verificar antes de operar
import sys
MAX_INT = sys.maxsize  # En Python, referencia para compatibilidad

def suma_segura(a, b, max_val=MAX_INT):
    if b > 0 and a > max_val - b:
        raise OverflowError("Suma causaría overflow")
    return a + b

# 3. Punto medio seguro (evita overflow en a + b)
def punto_medio(a, b):
    return a + (b - a) // 2  # En vez de (a + b) // 2
```

---

## Aplicaciones en Algoritmos

### 1. Fibonacci con Módulo

```python
def fibonacci_mod(n, mod=10**9 + 7):
    """Calcula F(n) % mod eficientemente"""
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, (a + b) % mod
    return b

print(fibonacci_mod(100))  # Sin problema de overflow
```

### 2. Suma de Rango con Divisibilidad

```python
def contar_divisibles_en_rango(inicio, fin, divisor):
    """Cuenta números divisibles por 'divisor' en [inicio, fin]"""
    # Cantidad hasta 'fin' menos cantidad hasta 'inicio-1'
    return fin // divisor - (inicio - 1) // divisor

print(contar_divisibles_en_rango(1, 100, 7))   # 14
print(contar_divisibles_en_rango(10, 50, 5))   # 9
```

### 3. Checksum Simple

```python
def checksum(data):
    """Calcula un checksum simple usando módulo"""
    total = sum(ord(c) for c in data)
    return total % 256

print(checksum("Hello"))  # 500 % 256 = 244
```

### 4. Hash Simple

```python
def hash_simple(s, mod=10**9 + 7):
    """Hash de string usando aritmética modular"""
    base = 31
    hash_val = 0
    for i, c in enumerate(s):
        hash_val += (ord(c) - ord('a') + 1) * pow(base, i, mod)
        hash_val %= mod
    return hash_val

print(hash_simple("abc"))
```

---

## Ejercicios Prácticos

### Nivel Básico

1. **Suma de Dígitos**
   ```python
   def suma_digitos(n):
       # Tu código aquí
       pass
   
   # Test: suma_digitos(12345) == 15
   ```

2. **Invertir Número**
   ```python
   def invertir_numero(n):
       # Tu código aquí
       pass
   
   # Test: invertir_numero(12345) == 54321
   ```

3. **Es Palíndromo Numérico**
   ```python
   def es_palindromo(n):
       # Tu código aquí
       pass
   
   # Test: es_palindromo(12321) == True
   ```

### Nivel Intermedio

4. **Máximo Común Divisor (sin usar math.gcd)**
   ```python
   def mcd(a, b):
       # Implementar algoritmo de Euclides
       pass
   
   # Test: mcd(48, 18) == 6
   ```

5. **Menor Común Múltiplo**
   ```python
   def mcm(a, b):
       # Usar: mcm(a,b) = a * b / mcd(a,b)
       pass
   
   # Test: mcm(4, 6) == 12
   ```

6. **Factorial con Módulo**
   ```python
   def factorial_mod(n, mod=10**9 + 7):
       # Tu código aquí
       pass
   
   # Test: factorial_mod(10) == 3628800
   ```

### Nivel Avanzado

7. **Exponenciación Rápida Manual**
   ```python
   def pow_rapido(base, exp, mod):
       # Implementar sin usar pow()
       pass
   
   # Test: pow_rapido(2, 10, 1000) == 24
   ```

8. **Contar Ceros Finales en Factorial**
   ```python
   def ceros_factorial(n):
       # Contar cuántos ceros tiene n! al final
       pass
   
   # Test: ceros_factorial(100) == 24
   ```

---

## Resumen

| Concepto | Complejidad | Uso Principal |
|----------|-------------|---------------|
| Operaciones básicas | O(1) | Todo algoritmo |
| Divisibilidad | O(√n) | Encontrar divisores |
| Módulo | O(1) | Evitar overflow, índices circulares |
| pow(a, n, m) | O(log n) | Exponenciación modular |
| GCD (Euclides) | O(log min(a,b)) | Simplificar fracciones |

---

## Recursos Adicionales

- 📖 [Khan Academy - Aritmética](https://es.khanacademy.org/math/arithmetic)
- 🎥 [3Blue1Brown - Visualización matemática](https://www.youtube.com/c/3blue1brown)
- 💻 [LeetCode - Problemas de matemáticas](https://leetcode.com/tag/math/)

---

<div align="center">

**Siguiente tema:** [Álgebra](../02-Algebra/)

</div>
