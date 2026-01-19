# 📦 Variables y Tipos de Datos

## 📋 Índice

1. [¿Qué es una Variable?](#1-qué-es-una-variable)
2. [Tipos de Datos Primitivos](#2-tipos-de-datos-primitivos)
3. [Tipos de Datos por Referencia](#3-tipos-de-datos-por-referencia)
4. [Sistemas de Tipado](#4-sistemas-de-tipado)
5. [Gestión de Memoria](#5-gestión-de-memoria)
6. [Scope y Tiempo de Vida](#6-scope-y-tiempo-de-vida)
7. [Constantes e Inmutabilidad](#7-constantes-e-inmutabilidad)
8. [Conversión de Tipos](#8-conversión-de-tipos)
9. [Conceptos Adicionales](#9-conceptos-adicionales)
10. [Conceptos Avanzados (Nivel Profesional)](#10-conceptos-avanzados-nivel-profesional)
11. [Mejores Prácticas Profesionales](#11-mejores-prácticas-profesionales)
12. [Preguntas de Entrevista](#12-preguntas-de-entrevista)

---

## 1. ¿Qué es una Variable?

### Definición

Una **variable** es un espacio de memoria con un nombre asociado que almacena un valor que puede cambiar durante la ejecución del programa.

### Componentes de una Variable

```
┌─────────────────────────────────────────┐
│            VARIABLE                      │
├─────────────────────────────────────────┤
│  Nombre (identificador): edad           │
│  Tipo: entero                           │
│  Valor: 25                              │
│  Dirección en memoria: 0x7FFE4          │
└─────────────────────────────────────────┘
```

### Declaración vs Inicialización

```pseudocode
// Declaración: reservar espacio en memoria
DECLARAR edad COMO Entero

// Inicialización: asignar un valor inicial
edad ← 25

// Declaración e inicialización juntas
DECLARAR nombre COMO Cadena ← "Juan"
```

### Reglas para Nombres de Variables

| Regla | Válido | Inválido |
|-------|--------|----------|
| Comenzar con letra o guión bajo | `edad`, `_contador` | `1variable` |
| No usar palabras reservadas | `miSi` | `SI`, `PARA` |
| Sin espacios | `miVariable` | `mi variable` |
| Case sensitive (depende del lenguaje) | `Edad` ≠ `edad` | - |

---

## 2. Tipos de Datos Primitivos

Los **tipos primitivos** son los bloques básicos de construcción. Se almacenan directamente en memoria y tienen un tamaño fijo.

### Tipos Numéricos Enteros

| Tipo | Tamaño | Rango | Ejemplo |
|------|--------|-------|---------|
| **byte** | 8 bits | -128 a 127 | `DECLARAR b COMO Byte ← 100` |
| **short** | 16 bits | -32,768 a 32,767 | `DECLARAR s COMO Short ← 1000` |
| **int** | 32 bits | -2.1×10⁹ a 2.1×10⁹ | `DECLARAR i COMO Entero ← 50000` |
| **long** | 64 bits | -9.2×10¹⁸ a 9.2×10¹⁸ | `DECLARAR l COMO Largo ← 9999999999` |

### Representación en Memoria

```
Entero de 32 bits para el número 25:
┌────┬────┬────┬────┬────┬────┬────┬────┐
│ 0  │ 0  │ 0  │ 0  │ 0  │ 0  │ 0  │ 0  │  Byte 1
├────┼────┼────┼────┼────┼────┼────┼────┤
│ 0  │ 0  │ 0  │ 0  │ 0  │ 0  │ 0  │ 0  │  Byte 2
├────┼────┼────┼────┼────┼────┼────┼────┤
│ 0  │ 0  │ 0  │ 0  │ 0  │ 0  │ 0  │ 0  │  Byte 3
├────┼────┼────┼────┼────┼────┼────┼────┤
│ 0  │ 0  │ 0  │ 1  │ 1  │ 0  │ 0  │ 1  │  Byte 4 = 25
└────┴────┴────┴────┴────┴────┴────┴────┘
```

### Tipos Numéricos Decimales (Punto Flotante)

| Tipo | Tamaño | Precisión | Ejemplo |
|------|--------|-----------|---------|
| **float** | 32 bits | ~7 dígitos | `DECLARAR f COMO Flotante ← 3.14` |
| **double** | 64 bits | ~15 dígitos | `DECLARAR d COMO Doble ← 3.14159265359` |

### Estándar IEEE 754 (Punto Flotante)

```
Estructura de un float de 32 bits:
┌───┬────────────┬───────────────────────┐
│ S │  Exponente │       Mantisa         │
│1b │   8 bits   │       23 bits         │
└───┴────────────┴───────────────────────┘

S = Signo (0 = positivo, 1 = negativo)
```

> ⚠️ **Cuidado:** Los números flotantes pueden tener errores de precisión.
> Ejemplo: 0.1 + 0.2 ≠ 0.3 exactamente en muchos sistemas.

### Tipo Carácter

```pseudocode
DECLARAR letra COMO Caracter ← 'A'
DECLARAR simbolo COMO Caracter ← '@'
```

| Codificación | Tamaño | Caracteres |
|--------------|--------|------------|
| ASCII | 7/8 bits | 128/256 caracteres |
| Unicode (UTF-8) | 1-4 bytes | >1 millón de caracteres |
| Unicode (UTF-16) | 2-4 bytes | >1 millón de caracteres |

### Tipo Booleano

Solo puede tener dos valores: **VERDADERO** o **FALSO**.

```pseudocode
DECLARAR esActivo COMO Booleano ← VERDADERO
DECLARAR esMayor COMO Booleano ← (edad >= 18)
```

### Resumen de Primitivos

```
┌─────────────────────────────────────────────────────┐
│              TIPOS PRIMITIVOS                        │
├─────────────────────────────────────────────────────┤
│  NUMÉRICOS                                          │
│  ├── Enteros: byte, short, int, long                │
│  └── Decimales: float, double                       │
│                                                     │
│  CARÁCTER                                           │
│  └── char                                           │
│                                                     │
│  LÓGICO                                             │
│  └── boolean (verdadero/falso)                      │
└─────────────────────────────────────────────────────┘
```

---

## 3. Tipos de Datos por Referencia

Los **tipos por referencia** no almacenan el valor directamente, sino una **dirección de memoria** (puntero) que apunta a donde está el valor real.

### Diferencia Visual

```
PRIMITIVO (almacena el valor directamente):
┌──────────────────┐
│  edad = 25       │  ← El valor 25 está aquí
│  [0x100]         │
└──────────────────┘

REFERENCIA (almacena una dirección):
┌──────────────────┐         ┌──────────────────┐
│  persona = 0x500 │ ──────► │  {nombre: "Ana"} │
│  [0x100]         │         │  [0x500]         │
└──────────────────┘         └──────────────────┘
     Variable                    Objeto en Heap
```

### Ejemplos de Tipos por Referencia

```pseudocode
// Arreglos
DECLARAR numeros COMO Arreglo[Entero] ← [1, 2, 3, 4, 5]

// Cadenas (en muchos lenguajes)
DECLARAR mensaje COMO Cadena ← "Hola Mundo"

// Objetos/Estructuras
DECLARAR persona COMO Persona ← NUEVO Persona("Ana", 25)

// Listas dinámicas
DECLARAR lista COMO Lista[Entero] ← NUEVA Lista()
```

### Comportamiento al Copiar

```pseudocode
// === PRIMITIVOS: Se copia el VALOR ===
DECLARAR a COMO Entero ← 10
DECLARAR b COMO Entero ← a      // b = 10
b ← 20                          // a sigue siendo 10

// === REFERENCIAS: Se copia la DIRECCIÓN ===
DECLARAR arr1 COMO Arreglo ← [1, 2, 3]
DECLARAR arr2 COMO Arreglo ← arr1    // arr2 apunta al mismo arreglo
arr2[0] ← 99                         // ¡arr1[0] también es 99!
```

### Visualización de la Copia

```
ANTES de arr2[0] ← 99:
┌──────────┐         ┌─────────────┐
│ arr1=0x50│ ──────► │ [1, 2, 3]   │
└──────────┘    ┌──► │  [0x500]    │
┌──────────┐    │    └─────────────┘
│ arr2=0x50│ ───┘
└──────────┘

DESPUÉS de arr2[0] ← 99:
┌──────────┐         ┌─────────────┐
│ arr1=0x50│ ──────► │ [99, 2, 3]  │  ← ¡Ambos ven el cambio!
└──────────┘    ┌──► │  [0x500]    │
┌──────────┐    │    └─────────────┘
│ arr2=0x50│ ───┘
└──────────┘
```

### Copia Superficial vs Copia Profunda

```pseudocode
// Copia superficial (shallow copy)
// Solo copia la referencia del primer nivel
arr2 ← COPIA_SUPERFICIAL(arr1)

// Copia profunda (deep copy)
// Copia todo, creando nuevos objetos
arr2 ← COPIA_PROFUNDA(arr1)
```

---

## 4. Sistemas de Tipado

### Tipado Estático vs Dinámico

| Característica | Tipado Estático | Tipado Dinámico |
|----------------|-----------------|-----------------|
| **Cuándo se verifica** | En compilación | En ejecución |
| **Declaración de tipo** | Obligatoria | Opcional/Automática |
| **Cambiar tipo** | No permitido | Permitido |
| **Errores** | Detectados antes | Detectados al ejecutar |
| **Ejemplos** | C, Java, C++ | Python, JavaScript, Ruby |

```pseudocode
// === TIPADO ESTÁTICO ===
DECLARAR edad COMO Entero ← 25
edad ← "veinticinco"    // ❌ ERROR en compilación

// === TIPADO DINÁMICO ===
edad ← 25               // edad es Entero
edad ← "veinticinco"    // ✓ edad ahora es Cadena
```

### Tipado Fuerte vs Débil

| Característica | Tipado Fuerte | Tipado Débil |
|----------------|---------------|--------------|
| **Conversión implícita** | Mínima/Ninguna | Frecuente |
| **Operaciones mixtas** | Error o explícitas | Permitidas |
| **Ejemplos** | Python, Java | JavaScript, PHP |

```pseudocode
// === TIPADO FUERTE ===
DECLARAR x COMO Entero ← 5
DECLARAR y COMO Cadena ← "3"
resultado ← x + y    // ❌ ERROR: no se puede sumar Entero + Cadena

// === TIPADO DÉBIL ===
resultado ← 5 + "3"  // ✓ Resultado: "53" (concatenación) o 8 (suma)
                     // Depende del lenguaje
```

### Inferencia de Tipos

Algunos lenguajes pueden **inferir** el tipo automáticamente:

```pseudocode
// Sin inferencia (explícito)
DECLARAR edad COMO Entero ← 25

// Con inferencia (el compilador deduce el tipo)
DECLARAR edad ← 25    // El compilador sabe que es Entero
```

---

## 5. Gestión de Memoria

### Regiones de Memoria

```
┌─────────────────────────────────────────────────────┐
│                MEMORIA DEL PROGRAMA                  │
├─────────────────────────────────────────────────────┤
│                                                     │
│   ┌─────────────────────────────────────────────┐   │
│   │              CÓDIGO (TEXT)                  │   │
│   │  Instrucciones del programa (solo lectura)  │   │
│   └─────────────────────────────────────────────┘   │
│                                                     │
│   ┌─────────────────────────────────────────────┐   │
│   │            DATOS ESTÁTICOS                  │   │
│   │  Variables globales, constantes             │   │
│   └─────────────────────────────────────────────┘   │
│                                                     │
│   ┌─────────────────────────────────────────────┐   │
│   │               HEAP (Montículo)              │   │
│   │  Memoria dinámica (objetos, arreglos)       │   │
│   │  Crece hacia abajo ↓                        │   │
│   │                                             │   │
│   │                    ↕                        │   │
│   │                                             │   │
│   │  Crece hacia arriba ↑                       │   │
│   │              STACK (Pila)                   │   │
│   │  Variables locales, llamadas a funciones    │   │
│   └─────────────────────────────────────────────┘   │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### Stack (Pila)

- **Almacena:** Variables locales, parámetros de funciones, direcciones de retorno
- **Gestión:** Automática (LIFO - Last In, First Out)
- **Tamaño:** Limitado (puede causar Stack Overflow)
- **Velocidad:** Muy rápida

```pseudocode
FUNCIÓN calcular(a, b)
    DECLARAR resultado COMO Entero    // Se crea en el Stack
    resultado ← a + b
    RETORNAR resultado
FIN FUNCIÓN                           // resultado se destruye automáticamente
```

```
Llamada: calcular(5, 3)

STACK:
┌─────────────────────┐
│  resultado = 8      │  ← Tope del stack
├─────────────────────┤
│  b = 3              │
├─────────────────────┤
│  a = 5              │
├─────────────────────┤
│  dirección retorno  │
└─────────────────────┘
```

### Heap (Montículo)

- **Almacena:** Objetos, arreglos dinámicos, datos de tamaño variable
- **Gestión:** Manual o por Garbage Collector
- **Tamaño:** Grande (limitado por RAM)
- **Velocidad:** Más lenta que Stack

```pseudocode
FUNCIÓN crearPersona(nombre)
    // El objeto se crea en el Heap
    DECLARAR p COMO Persona ← NUEVO Persona(nombre)
    RETORNAR p    // La referencia se retorna, el objeto persiste
FIN FUNCIÓN
```

### Garbage Collection (Recolección de Basura)

Sistema automático que libera memoria de objetos que ya no son accesibles.

```pseudocode
FUNCIÓN ejemplo()
    DECLARAR obj COMO Objeto ← NUEVO Objeto()
    obj ← NULO    // El objeto original ya no es accesible
FIN FUNCIÓN       // El Garbage Collector lo limpiará eventualmente
```

### Memory Leaks (Fugas de Memoria)

Ocurren cuando la memoria reservada nunca se libera:

```pseudocode
// ❌ FUGA DE MEMORIA
MIENTRAS VERDADERO HACER
    DECLARAR datos COMO Arreglo ← NUEVO Arreglo(1000000)
    // El arreglo nunca se libera y sigue reservando memoria
FIN MIENTRAS
```

---

## 6. Scope y Tiempo de Vida

### Scope (Ámbito)

El **scope** define dónde una variable es accesible.

```pseudocode
DECLARAR global COMO Entero ← 100    // Scope: todo el programa

FUNCIÓN miFuncion()
    DECLARAR local COMO Entero ← 50  // Scope: solo dentro de miFuncion
    
    SI local > 0 ENTONCES
        DECLARAR bloque COMO Entero ← 25  // Scope: solo dentro del SI
        ESCRIBIR(global)    // ✓ Accesible
        ESCRIBIR(local)     // ✓ Accesible
        ESCRIBIR(bloque)    // ✓ Accesible
    FIN SI
    
    ESCRIBIR(bloque)        // ❌ ERROR: fuera de scope
FIN FUNCIÓN

ESCRIBIR(local)             // ❌ ERROR: fuera de scope
```

### Niveles de Scope

```
┌─────────────────────────────────────────────────────┐
│  SCOPE GLOBAL                                        │
│  ┌───────────────────────────────────────────────┐  │
│  │  SCOPE DE FUNCIÓN                             │  │
│  │  ┌─────────────────────────────────────────┐  │  │
│  │  │  SCOPE DE BLOQUE                        │  │  │
│  │  │  (if, for, while, etc.)                 │  │  │
│  │  └─────────────────────────────────────────┘  │  │
│  └───────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────┘
```

### Tiempo de Vida (Lifetime)

| Tipo de Variable | Tiempo de Vida |
|------------------|----------------|
| **Global** | Toda la ejecución del programa |
| **Local** | Mientras la función está en ejecución |
| **De bloque** | Mientras el bloque está en ejecución |
| **Dinámica (Heap)** | Hasta que se libera explícitamente o por GC |

### Shadowing (Sombreado)

Una variable local puede "ocultar" una variable de scope superior:

```pseudocode
DECLARAR x COMO Entero ← 10    // x global

FUNCIÓN miFuncion()
    DECLARAR x COMO Entero ← 20    // x local "sombrea" a x global
    ESCRIBIR(x)                     // Imprime: 20
FIN FUNCIÓN

ESCRIBIR(x)                         // Imprime: 10
```

---

## 7. Constantes e Inmutabilidad

### Constantes

Variables cuyo valor no puede cambiar después de la asignación inicial.

```pseudocode
CONSTANTE PI ← 3.14159
CONSTANTE MAX_USUARIOS ← 1000

PI ← 3.14    // ❌ ERROR: no se puede modificar una constante
```

### Inmutabilidad

Un objeto **inmutable** no puede ser modificado después de su creación.

```pseudocode
// Cadenas inmutables (en muchos lenguajes)
DECLARAR texto COMO Cadena ← "Hola"
texto ← texto + " Mundo"    // Crea una NUEVA cadena, no modifica la original
```

```
Antes:
texto ──► "Hola" [0x100]

Después:
texto ──► "Hola Mundo" [0x200]    // Nueva cadena
          "Hola" [0x100]          // La original sigue existiendo
                                  // (será eliminada por GC)
```

### Ventajas de la Inmutabilidad

1. **Thread-safe:** No hay problemas de concurrencia
2. **Predecible:** El valor nunca cambia inesperadamente
3. **Hashable:** Puede usarse como clave en diccionarios

---

## 8. Conversión de Tipos

### Conversión Implícita (Coerción)

El sistema convierte automáticamente cuando no hay pérdida de información:

```pseudocode
DECLARAR entero COMO Entero ← 10
DECLARAR decimal COMO Doble ← entero    // ✓ Implícita: 10 → 10.0
```

```
Jerarquía de conversión implícita (widening):
byte → short → int → long → float → double
```

### Conversión Explícita (Casting)

Necesaria cuando puede haber pérdida de información:

```pseudocode
DECLARAR decimal COMO Doble ← 9.7
DECLARAR entero COMO Entero ← (Entero) decimal    // Explícita: 9.7 → 9
                                                   // Se pierde la parte decimal
```

### Conversión de Cadenas

```pseudocode
// Número a Cadena
DECLARAR num COMO Entero ← 42
DECLARAR texto COMO Cadena ← CONVERTIR_A_CADENA(num)    // "42"

// Cadena a Número
DECLARAR texto COMO Cadena ← "123"
DECLARAR num COMO Entero ← CONVERTIR_A_ENTERO(texto)    // 123
```

---

## 9. Conceptos Adicionales

### Valor Nulo (Null/None/Nil)

Representa la **ausencia de valor** o una referencia que no apunta a nada.

```pseudocode
DECLARAR persona COMO Persona ← NULO

SI persona = NULO ENTONCES
    ESCRIBIR("No hay persona asignada")
FIN SI

persona.nombre    // ❌ ERROR: NullPointerException / NullReferenceError
```

### Valores por Defecto

Cuando una variable no se inicializa explícitamente:

| Tipo | Valor por Defecto |
|------|-------------------|
| Enteros | 0 |
| Flotantes | 0.0 |
| Booleanos | FALSO |
| Caracteres | '\0' (carácter nulo) |
| Referencias | NULO |

### Paso por Valor vs Paso por Referencia

```pseudocode
// === PASO POR VALOR ===
FUNCIÓN duplicar(x)
    x ← x * 2
FIN FUNCIÓN

DECLARAR num ← 5
duplicar(num)
ESCRIBIR(num)    // Imprime: 5 (no cambió)

// === PASO POR REFERENCIA ===
FUNCIÓN duplicarRef(REF x)
    x ← x * 2
FIN FUNCIÓN

DECLARAR num ← 5
duplicarRef(num)
ESCRIBIR(num)    // Imprime: 10 (cambió)
```

### Alias

Cuando múltiples nombres se refieren al mismo espacio de memoria:

```pseudocode
DECLARAR lista1 COMO Lista ← [1, 2, 3]
DECLARAR lista2 COMO Lista ← lista1    // lista2 es un ALIAS de lista1

lista2.agregar(4)
ESCRIBIR(lista1)    // [1, 2, 3, 4] - ¡lista1 también cambió!
```

---

## 📝 Resumen Visual

```
┌─────────────────────────────────────────────────────────────┐
│                    TIPOS DE DATOS                            │
├──────────────────────────┬──────────────────────────────────┤
│       PRIMITIVOS         │         POR REFERENCIA           │
├──────────────────────────┼──────────────────────────────────┤
│ • Enteros                │ • Arreglos                       │
│ • Flotantes              │ • Cadenas*                       │
│ • Caracteres             │ • Objetos/Estructuras            │
│ • Booleanos              │ • Listas                         │
├──────────────────────────┼──────────────────────────────────┤
│ Almacenados en: STACK    │ Referencia en: STACK             │
│                          │ Objeto en: HEAP                  │
├──────────────────────────┼──────────────────────────────────┤
│ Copia: El VALOR          │ Copia: La DIRECCIÓN              │
└──────────────────────────┴──────────────────────────────────┘

* Depende del lenguaje
```

---

## 📚 Ejercicios

1. ¿Qué valor tendrá `b` después de ejecutar?
   ```pseudocode
   DECLARAR a ← 10
   DECLARAR b ← a
   a ← 20
   ```

2. ¿Qué valor tendrá `arr1[0]` después de ejecutar?
   ```pseudocode
   DECLARAR arr1 ← [1, 2, 3]
   DECLARAR arr2 ← arr1
   arr2[0] ← 99
   ```

3. Identifica el error:
   ```pseudocode
   DECLARAR x COMO Entero ← "hola"
   ```

4. ¿Es válido en un lenguaje con tipado dinámico?
   ```pseudocode
   x ← 10
   x ← "diez"
   ```

---

## 10. Conceptos Avanzados

### Endianness (Orden de Bytes)

Define cómo se almacenan los bytes de un número en memoria.

```
Número: 0x12345678 (4 bytes)

BIG ENDIAN (más significativo primero):
┌──────┬──────┬──────┬──────┐
│ 0x12 │ 0x34 │ 0x56 │ 0x78 │
└──────┴──────┴──────┴──────┘
Dirección:  0      1      2      3

LITTLE ENDIAN (menos significativo primero):
┌──────┬──────┬──────┬──────┐
│ 0x78 │ 0x56 │ 0x34 │ 0x12 │
└──────┴──────┴──────┴──────┘
Dirección:  0      1      2      3
```

**¿Por qué importa?**
- Transferencia de datos entre sistemas
- Lectura/escritura de archivos binarios
- Protocolos de red (Network Byte Order = Big Endian)

---

### Memory Alignment (Alineación de Memoria)

Los procesadores acceden a memoria más eficientemente cuando los datos están **alineados** a múltiplos de su tamaño.

```
❌ SIN ALINEACIÓN (más lento):
┌────┬────┬────┬────┬────┬────┬────┬────┐
│ a  │ b  │ b  │ b  │ b  │ c  │    │    │
└────┴────┴────┴────┴────┴────┴────┴────┘
  0    1    2    3    4    5    6    7

✓ CON ALINEACIÓN (más rápido):
┌────┬────┬────┬────┬────┬────┬────┬────┐
│ a  │PADD│PADD│PADD│ b  │ b  │ b  │ b  │
└────┴────┴────┴────┴────┴────┴────┴────┘
  0    1    2    3    4    5    6    7
                     └── b alineado a 4 bytes
```

**Regla general:** Un dato de N bytes debe empezar en una dirección múltiplo de N.

---

### Padding (Relleno)

Bytes extra agregados para mantener la alineación.

```pseudocode
ESTRUCTURA Ejemplo
    a COMO Byte         // 1 byte
    // 3 bytes de padding
    b COMO Entero       // 4 bytes
    c COMO Byte         // 1 byte  
    // 3 bytes de padding
FIN ESTRUCTURA

// Tamaño esperado: 1 + 4 + 1 = 6 bytes
// Tamaño real: 12 bytes (con padding)
```

```
┌────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┐
│ a  │PAD │PAD │PAD │  b │  b │  b │  b │ c  │PAD │PAD │PAD │
└────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┘
```

**Optimización:** Ordenar campos de mayor a menor reduce el padding.

---

### Boxing y Unboxing

Conversión entre tipos primitivos y sus equivalentes como objetos.

```pseudocode
// BOXING: primitivo → objeto (wrapper)
DECLARAR num COMO Entero ← 42
DECLARAR obj COMO Objeto ← EMPAQUETAR(num)    // Boxing

// UNBOXING: objeto → primitivo  
DECLARAR valor COMO Entero ← DESEMPAQUETAR(obj)    // Unboxing
```

```
BOXING:
┌─────────────┐                ┌─────────────────────┐
│  num = 42   │ ──BOXING──►   │  IntegerObject      │
│  (Stack)    │                │  valor: 42          │
└─────────────┘                │  (Heap)             │
                               └─────────────────────┘

UNBOXING:
┌─────────────────────┐                ┌─────────────┐
│  IntegerObject      │ ──UNBOXING──►  │  valor = 42 │
│  valor: 42          │                │  (Stack)    │
└─────────────────────┘                └─────────────┘
```

**Costo de performance:**
- Boxing asigna memoria en el Heap
- Unboxing requiere verificación de tipo
- Evitar en bucles de alto rendimiento

---

### Tipos Genéricos (Generics)

Permiten crear código reutilizable que funciona con diferentes tipos.

```pseudocode
// Sin genéricos: necesitas una clase por cada tipo
CLASE ListaEnteros
    datos COMO Arreglo[Entero]
    ...
FIN CLASE

CLASE ListaCadenas
    datos COMO Arreglo[Cadena]
    ...
FIN CLASE

// Con genéricos: una sola clase para todos los tipos
CLASE Lista<T>
    datos COMO Arreglo[T]
    
    FUNCIÓN agregar(elemento COMO T)
        ...
    FIN FUNCIÓN
    
    FUNCIÓN obtener(índice) RETORNA T
        RETORNAR datos[índice]
    FIN FUNCIÓN
FIN CLASE

// Uso
DECLARAR numeros COMO Lista<Entero> ← NUEVA Lista<Entero>()
DECLARAR nombres COMO Lista<Cadena> ← NUEVA Lista<Cadena>()
```

**Ventajas:**
- Reutilización de código
- Type safety en tiempo de compilación
- Evita casting manual

---

### Tipos Nullable

Tipos que pueden contener un valor O ser nulos de forma explícita y segura.

```pseudocode
// Sin nullable: el nulo es implícito y peligroso
DECLARAR edad COMO Entero ← NULO    // ¿Es válido? Depende del lenguaje

// Con nullable: el nulo es explícito
DECLARAR edad COMO Entero? ← NULO   // Claramente puede ser nulo
DECLARAR altura COMO Entero ← 170   // NO puede ser nulo

// Uso seguro
SI edad TIENE_VALOR ENTONCES
    ESCRIBIR("Edad: " + edad.VALOR)
SINO
    ESCRIBIR("Edad no especificada")
FIN SI
```

**Operadores comunes:**
```pseudocode
// Operador de coalescencia nula (??)
resultado ← valorPosiblementeNulo ?? valorPorDefecto

// "Si edad es nulo, usar 0"
edadReal ← edad ?? 0

// Operador de acceso seguro (?.)
// "Si persona no es nula, acceder a nombre"
nombre ← persona?.nombre    // Retorna NULO si persona es NULO
```

---

### Tipos de Unión y Suma (Union Types)

Un valor puede ser de uno de varios tipos posibles.

```pseudocode
// Tipo unión: puede ser Entero O Cadena
DECLARAR id COMO Entero | Cadena

id ← 123          // ✓ Válido
id ← "ABC-456"    // ✓ Válido
id ← 3.14         // ❌ Error: no es Entero ni Cadena

// Uso con verificación de tipo
SI id ES Entero ENTONCES
    ESCRIBIR("ID numérico: " + id)
SINO SI id ES Cadena ENTONCES
    ESCRIBIR("ID texto: " + id)
FIN SI
```

---

### Tipos Algebraicos (Enums Avanzados)

Enumeraciones que pueden contener datos asociados.

```pseudocode
TIPO Resultado
    | Exito(valor COMO Entero)
    | Error(mensaje COMO Cadena)
FIN TIPO

FUNCIÓN dividir(a, b) RETORNA Resultado
    SI b = 0 ENTONCES
        RETORNAR Error("División por cero")
    SINO
        RETORNAR Exito(a / b)
    FIN SI
FIN FUNCIÓN

// Uso con pattern matching
SEGÚN dividir(10, 2) HACER
    CASO Exito(v):
        ESCRIBIR("Resultado: " + v)
    CASO Error(msg):
        ESCRIBIR("Error: " + msg)
FIN SEGÚN
```

---

## 11. Mejores Prácticas Profesionales

### ✅ Buenas Prácticas

```pseudocode
// 1. Nombres descriptivos
✓ DECLARAR edadUsuario COMO Entero
✗ DECLARAR e COMO Entero

// 2. Inicializar siempre
✓ DECLARAR contador COMO Entero ← 0
✗ DECLARAR contador COMO Entero    // Valor indefinido

// 3. Usar constantes para valores mágicos
✓ CONSTANTE DIAS_SEMANA ← 7
  SI dias > DIAS_SEMANA ENTONCES ...
✗ SI dias > 7 ENTONCES ...

// 4. Minimizar el scope
✓ Declarar variables lo más cerca posible de su uso
✗ Declarar todas las variables al inicio de la función

// 5. Preferir inmutabilidad cuando sea posible
✓ CONSTANTE configuracion ← cargarConfig()
✗ DECLARAR configuracion ← cargarConfig()  // Si nunca cambia
```

### ❌ Anti-patrones Comunes

```pseudocode
// 1. Variables globales excesivas
✗ GLOBAL contadorGlobal ← 0    // Difícil de rastrear y testear

// 2. Nombres genéricos
✗ DECLARAR data, temp, aux, x, i2

// 3. Reusar variables para propósitos diferentes
✗ resultado ← calcularPrecio()
  resultado ← "Operación completada"    // Cambio de propósito

// 4. No verificar nulos
✗ ESCRIBIR(usuario.nombre)    // ¿Y si usuario es NULO?

// 5. Confiar en valores por defecto implícitos
✗ DECLARAR activo COMO Booleano    // ¿Es FALSO o indefinido?
```

---

## 12. Preguntas de Entrevista

### Preguntas Frecuentes

1. **¿Cuál es la diferencia entre paso por valor y paso por referencia?**
   > En paso por valor se copia el valor, cambios no afectan al original.
   > En paso por referencia se pasa la dirección, cambios sí afectan al original.

2. **¿Qué es un memory leak y cómo se previene?**
   > Es memoria reservada que nunca se libera. Se previene con gestión adecuada
   > de referencias, usando Garbage Collection o liberando memoria manualmente.

3. **¿Por qué 0.1 + 0.2 ≠ 0.3 en punto flotante?**
   > Porque la representación binaria de decimales como 0.1 es periódica infinita,
   > similar a 1/3 = 0.333... en decimal. Se pierde precisión al truncar.

4. **¿Stack vs Heap?**
   > Stack: rápido, automático, limitado, datos de tamaño fijo.
   > Heap: más lento, manual/GC, grande, datos dinámicos.

5. **¿Qué es boxing y por qué puede ser problemático?**
   > Es convertir un primitivo a objeto. Es costoso porque asigna memoria
   > en el Heap y requiere verificación de tipo al desempaquetar.

### Ejercicio de Entrevista

```pseudocode
// ¿Qué imprime este código?
FUNCIÓN modificar(arr, num)
    arr[0] ← 999
    num ← 999
FIN FUNCIÓN

DECLARAR miArreglo ← [1, 2, 3]
DECLARAR miNumero ← 5

modificar(miArreglo, miNumero)

ESCRIBIR(miArreglo[0])    // ¿?
ESCRIBIR(miNumero)        // ¿?
```

<details>
<summary>Ver respuesta</summary>

```
miArreglo[0] = 999  // El arreglo se modifica (referencia)
miNumero = 5        // El número NO cambia (valor)
```
</details>

---

## 📊 Resumen de Complejidades

| Operación | Stack | Heap |
|-----------|-------|------|
| Asignar | O(1) | O(1) a O(n)* |
| Acceder | O(1) | O(1) |
| Liberar | O(1) automático | O(1) a O(n)* |

*Depende del Garbage Collector y fragmentación

---

## 🔗 Conexiones con Otros Temas

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   Variables y Tipos de Datos                                │
│           │                                                 │
│           ├──► Estructuras de Datos (Arreglos, Listas)      │
│           │                                                 │
│           ├──► Gestión de Memoria (Stack, Heap, GC)         │
│           │                                                 │
│           ├──► Punteros y Referencias                       │
│           │                                                 │
│           ├──► Programación Orientada a Objetos             │
│           │                                                 │
│           └──► Concurrencia (Thread Safety, Inmutabilidad)  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

**Siguiente tema:** [Operadores](../02-Operadores/)
