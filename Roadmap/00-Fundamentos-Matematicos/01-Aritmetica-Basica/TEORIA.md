# 📐 Aritmética Básica - Teoría Matemática

## 📋 Índice

1. [Números Naturales y Enteros](#1-números-naturales-y-enteros)
2. [Operaciones Fundamentales](#2-operaciones-fundamentales)
3. [Divisibilidad](#3-divisibilidad)
4. [División Euclídea](#4-división-euclídea)
5. [Propiedades de las Operaciones](#5-propiedades-de-las-operaciones)
6. [Potenciación y Radicación](#6-potenciación-y-radicación)
7. [Teoremas Fundamentales](#7-teoremas-fundamentales)

---

## 1. Números Naturales y Enteros

### Definiciones

**Números Naturales** $(\mathbb{N})$: Conjunto de números para contar.

$$\mathbb{N} = \{1, 2, 3, 4, 5, ...\}$$

> Nota: Algunos autores incluyen el 0 en $\mathbb{N}$, denotado como $\mathbb{N}_0 = \{0, 1, 2, 3, ...\}$

**Números Enteros** $(\mathbb{Z})$: Incluye negativos, cero y positivos.

$$\mathbb{Z} = \{..., -3, -2, -1, 0, 1, 2, 3, ...\}$$

### Axiomas de Peano (para $\mathbb{N}$)

1. $1 \in \mathbb{N}$ (1 es un número natural)
2. Si $n \in \mathbb{N}$, entonces $n + 1 \in \mathbb{N}$ (todo natural tiene un sucesor)
3. No existe $n \in \mathbb{N}$ tal que $n + 1 = 1$ (1 no es sucesor de ningún natural)
4. Si $n + 1 = m + 1$, entonces $n = m$ (el sucesor es único)
5. **Principio de Inducción:** Si un conjunto $S$ contiene a 1 y para todo $n \in S$ también contiene a $n+1$, entonces $S = \mathbb{N}$

---

## 2. Operaciones Fundamentales

### Suma

**Definición:** La suma es una operación binaria que asigna a cada par ordenado $(a, b)$ un único número $c = a + b$.

$$a + b = c$$

### Resta

**Definición:** La resta es la operación inversa de la suma.

$$a - b = c \iff a = b + c$$

### Multiplicación

**Definición:** La multiplicación es una suma repetida.

$$a \times b = \underbrace{a + a + a + ... + a}_{b \text{ veces}}$$

**Notación alternativa:** $a \cdot b$ o simplemente $ab$

### División

**Definición:** La división es la operación inversa de la multiplicación.

$$a \div b = c \iff a = b \times c \quad (b \neq 0)$$

**Notación alternativa:** $\frac{a}{b}$ o $a/b$

---

## 3. Divisibilidad

### Definición Formal

Sean $a, b \in \mathbb{Z}$ con $b \neq 0$. Decimos que **$b$ divide a $a$** (o que $a$ es divisible por $b$) si existe $k \in \mathbb{Z}$ tal que:

$$a = b \cdot k$$

**Notación:** $b \mid a$ (se lee "$b$ divide a $a$")

**Negación:** $b \nmid a$ significa "$b$ no divide a $a$"

### Ejemplos

- $3 \mid 12$ porque $12 = 3 \times 4$
- $5 \mid 0$ porque $0 = 5 \times 0$
- $7 \nmid 15$ porque no existe entero $k$ tal que $15 = 7k$

### Propiedades de la Divisibilidad

Sean $a, b, c, d \in \mathbb{Z}$:

1. **Reflexiva:** $a \mid a$ para todo $a \neq 0$

2. **Transitiva:** Si $a \mid b$ y $b \mid c$, entonces $a \mid c$

3. **Combinación lineal:** Si $d \mid a$ y $d \mid b$, entonces $d \mid (ax + by)$ para todo $x, y \in \mathbb{Z}$

4. **Multiplicación:** Si $a \mid b$, entonces $a \mid bc$ para todo $c \in \mathbb{Z}$

5. **Comparación:** Si $a \mid b$ y $b \neq 0$, entonces $|a| \leq |b|$

6. **Unidad:** $1 \mid a$ y $(-1) \mid a$ para todo $a \in \mathbb{Z}$

### Divisores

**Definición:** Un divisor de $n$ es cualquier entero $d$ tal que $d \mid n$.

**Divisores de 12:** $\{1, 2, 3, 4, 6, 12\}$ (positivos) o $\{\pm1, \pm2, \pm3, \pm4, \pm6, \pm12\}$ (todos)

### Criterios de Divisibilidad

| Divisor | Criterio |
|---------|----------|
| **2** | El último dígito es par (0, 2, 4, 6, 8) |
| **3** | La suma de los dígitos es divisible por 3 |
| **4** | Los dos últimos dígitos forman un número divisible por 4 |
| **5** | El último dígito es 0 o 5 |
| **6** | Es divisible por 2 y por 3 |
| **8** | Los tres últimos dígitos forman un número divisible por 8 |
| **9** | La suma de los dígitos es divisible por 9 |
| **10** | El último dígito es 0 |
| **11** | La suma alternada de dígitos es divisible por 11 |

---

## 4. División Euclídea

### Teorema de la División

**Teorema:** Para todo $a \in \mathbb{Z}$ y $b \in \mathbb{Z}^+$, existen únicos $q, r \in \mathbb{Z}$ tales que:

$$a = bq + r \quad \text{donde } 0 \leq r < b$$

**Donde:**
- $a$ = dividendo
- $b$ = divisor
- $q$ = cociente (del latín "quotient")
- $r$ = resto o residuo

### El Operador Módulo

**Definición:** El resto de dividir $a$ entre $b$ se denota:

$$r = a \mod b$$

o equivalentemente:

$$a \equiv r \pmod{b}$$

### Ejemplos

| División | Cociente ($q$) | Resto ($r$) | Verificación |
|----------|----------------|-------------|--------------|
| $17 \div 5$ | $3$ | $2$ | $17 = 5(3) + 2$ |
| $23 \div 7$ | $3$ | $2$ | $23 = 7(3) + 2$ |
| $100 \div 11$ | $9$ | $1$ | $100 = 11(9) + 1$ |

### Propiedades del Módulo

Sean $a, b, n \in \mathbb{Z}$ con $n > 0$:

1. $(a + b) \mod n = ((a \mod n) + (b \mod n)) \mod n$

2. $(a - b) \mod n = ((a \mod n) - (b \mod n) + n) \mod n$

3. $(a \times b) \mod n = ((a \mod n) \times (b \mod n)) \mod n$

4. $a \mod n = b \mod n \iff n \mid (a - b)$

---

## 5. Propiedades de las Operaciones

### Propiedades de la Suma en $\mathbb{Z}$

| Propiedad | Enunciado | Ejemplo |
|-----------|-----------|---------|
| **Clausura** | $a + b \in \mathbb{Z}$ | $3 + 5 = 8 \in \mathbb{Z}$ |
| **Conmutativa** | $a + b = b + a$ | $3 + 5 = 5 + 3$ |
| **Asociativa** | $(a + b) + c = a + (b + c)$ | $(2+3)+4 = 2+(3+4)$ |
| **Elemento neutro** | $a + 0 = a$ | $7 + 0 = 7$ |
| **Elemento opuesto** | $a + (-a) = 0$ | $5 + (-5) = 0$ |

### Propiedades de la Multiplicación en $\mathbb{Z}$

| Propiedad | Enunciado | Ejemplo |
|-----------|-----------|---------|
| **Clausura** | $a \times b \in \mathbb{Z}$ | $3 \times 5 = 15 \in \mathbb{Z}$ |
| **Conmutativa** | $a \times b = b \times a$ | $3 \times 5 = 5 \times 3$ |
| **Asociativa** | $(a \times b) \times c = a \times (b \times c)$ | $(2 \times 3) \times 4 = 2 \times (3 \times 4)$ |
| **Elemento neutro** | $a \times 1 = a$ | $7 \times 1 = 7$ |
| **Elemento absorbente** | $a \times 0 = 0$ | $7 \times 0 = 0$ |

### Propiedad Distributiva

$$a \times (b + c) = a \times b + a \times c$$

**Ejemplo:** $3 \times (4 + 5) = 3 \times 4 + 3 \times 5 = 12 + 15 = 27$

### Ley de los Signos

| Operación | Resultado |
|-----------|-----------|
| $(+) \times (+)$ | $+$ |
| $(+) \times (-)$ | $-$ |
| $(-) \times (+)$ | $-$ |
| $(-) \times (-)$ | $+$ |

---

## 6. Potenciación y Radicación

### Potenciación

**Definición:** Para $a \in \mathbb{R}$ y $n \in \mathbb{N}$:

$$a^n = \underbrace{a \times a \times a \times ... \times a}_{n \text{ factores}}$$

**Casos especiales:**
- $a^0 = 1$ para $a \neq 0$
- $a^1 = a$
- $0^n = 0$ para $n > 0$
- $0^0$ es indeterminado

### Propiedades de la Potenciación

Sean $a, b \in \mathbb{R}$ y $m, n \in \mathbb{Z}$:

1. **Producto de potencias:** $a^m \times a^n = a^{m+n}$

2. **Cociente de potencias:** $\frac{a^m}{a^n} = a^{m-n}$ para $a \neq 0$

3. **Potencia de potencia:** $(a^m)^n = a^{m \times n}$

4. **Potencia de un producto:** $(a \times b)^n = a^n \times b^n$

5. **Potencia de un cociente:** $\left(\frac{a}{b}\right)^n = \frac{a^n}{b^n}$ para $b \neq 0$

6. **Exponente negativo:** $a^{-n} = \frac{1}{a^n}$ para $a \neq 0$

### Radicación

**Definición:** La raíz $n$-ésima de $a$ es el número $b$ tal que $b^n = a$:

$$\sqrt[n]{a} = b \iff b^n = a$$

**Propiedades:**

1. $\sqrt[n]{a \times b} = \sqrt[n]{a} \times \sqrt[n]{b}$

2. $\sqrt[n]{\frac{a}{b}} = \frac{\sqrt[n]{a}}{\sqrt[n]{b}}$

3. $\sqrt[n]{a^m} = a^{m/n}$

4. $\sqrt[m]{\sqrt[n]{a}} = \sqrt[m \times n]{a}$

---

## 7. Teoremas Fundamentales

### Máximo Común Divisor (MCD)

**Definición:** El MCD de $a$ y $b$ es el mayor entero positivo que divide a ambos.

$$\text{mcd}(a, b) = \max\{d \in \mathbb{Z}^+ : d \mid a \text{ y } d \mid b\}$$

**Notación alternativa:** $\gcd(a, b)$ (del inglés "greatest common divisor")

**Propiedades:**
- $\text{mcd}(a, b) = \text{mcd}(b, a)$
- $\text{mcd}(a, 0) = |a|$
- $\text{mcd}(a, b) = \text{mcd}(a - b, b)$ si $a > b$
- $\text{mcd}(a, b) = \text{mcd}(a \mod b, b)$

### Mínimo Común Múltiplo (MCM)

**Definición:** El MCM de $a$ y $b$ es el menor entero positivo que es múltiplo de ambos.

$$\text{mcm}(a, b) = \min\{m \in \mathbb{Z}^+ : a \mid m \text{ y } b \mid m\}$$

**Relación fundamental:**

$$\text{mcd}(a, b) \times \text{mcm}(a, b) = |a \times b|$$

### Algoritmo de Euclides

Para calcular $\text{mcd}(a, b)$ con $a \geq b > 0$:

1. Si $b = 0$, entonces $\text{mcd}(a, b) = a$
2. Si no, calcular $\text{mcd}(b, a \mod b)$

**Ejemplo:** $\text{mcd}(48, 18)$

$$48 = 18 \times 2 + 12$$
$$18 = 12 \times 1 + 6$$
$$12 = 6 \times 2 + 0$$

Por lo tanto: $\text{mcd}(48, 18) = 6$

### Identidad de Bézout

**Teorema:** Para todo $a, b \in \mathbb{Z}$ no ambos cero, existen $x, y \in \mathbb{Z}$ tales que:

$$ax + by = \text{mcd}(a, b)$$

**Ejemplo:** Para $a = 48$ y $b = 18$, tenemos $\text{mcd}(48, 18) = 6$

Podemos encontrar: $48 \times (-1) + 18 \times 3 = -48 + 54 = 6$ ✓

---

## 📝 Ejercicios Propuestos

### Nivel Básico

1. Calcular la suma de los dígitos de $123456789$.

2. Determinar si $2847$ es divisible por 3 y por 9.

3. Hallar todos los divisores positivos de 36.

### Nivel Intermedio

4. Calcular $\text{mcd}(252, 198)$ usando el algoritmo de Euclides.

5. Encontrar $x, y \in \mathbb{Z}$ tales que $252x + 198y = \text{mcd}(252, 198)$.

6. Demostrar que si $n$ es impar, entonces $n^2$ es impar.

### Nivel Avanzado

7. Demostrar que $\text{mcd}(a, b) = \text{mcd}(a + b, \text{mcm}(a, b))$.

8. Probar que para todo $n \in \mathbb{N}$: $1 + 2 + 3 + ... + n = \frac{n(n+1)}{2}$ usando inducción.

---

## 📚 Referencias

- Hardy, G.H. & Wright, E.M. - *An Introduction to the Theory of Numbers*
- Rosen, Kenneth H. - *Elementary Number Theory*
- Burton, David M. - *Elementary Number Theory*
