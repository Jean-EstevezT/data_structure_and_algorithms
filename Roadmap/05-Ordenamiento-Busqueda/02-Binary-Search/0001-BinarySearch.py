import unittest

# Usa la fuerza bruta

# BusquWeda Binaria
def BinaryScan(arr, target):
    """
    Realiza una búsqueda binaria en un arreglo ordenado para encontrar un elemento objetivo.

    La búsqueda binaria es un algoritmo eficiente que funciona en arreglos ordenados.
    Compara el elemento objetivo con el elemento en el medio del arreglo.
    Si son iguales, se devuelve el índice. Si el objetivo es menor, la búsqueda
    continúa en la mitad inferior del arreglo. Si el objetivo es mayor, la búsqueda

    continúa en la mitad superior. Este proceso se repite hasta que se encuentra
    el elemento o se determina que no está en el arreglo.

    Args:
        arr (list): Una lista ordenada de elementos.
        target: El elemento a buscar en la lista.

    Returns:
        El elemento si se encuentra; de lo contrario, None.
    """
    low = 0
    high = len(arr) - 1
    # Controla la parte donde se va a buscar

    while low <= high:
        mid = (low + high) // 2  # comprobar la parte media
        guess = arr[mid]  # elemento medio
        if guess == target:
            # item encontrado
            return guess
        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return None

class TestBinaryScan(unittest.TestCase):
    def test_found(self):
        """Prueba que el elemento es encontrado si existe en la lista."""
        arr = [1, 3, 5, 7, 9, 11, 13, 15]
        self.assertEqual(BinaryScan(arr, 7), 7)

    def test_not_found(self):
        """Prueba que devuelve None si el elemento no está en la lista."""
        arr = [1, 3, 5, 7, 9, 11, 13, 15]
        self.assertIsNone(BinaryScan(arr, 4))

    def test_empty_list(self):
        """Prueba con una lista vacía."""
        arr = []
        self.assertIsNone(BinaryScan(arr, 5))

    def test_first_element(self):
        """Prueba encontrando el primer elemento de la lista."""
        arr = [2, 4, 6, 8, 10]
        self.assertEqual(BinaryScan(arr, 2), 2)

    def test_last_element(self):
        """Prueba encontrando el último elemento de la lista."""
        arr = [2, 4, 6, 8, 10]
        self.assertEqual(BinaryScan(arr, 10), 10)

if __name__ == '__main__':
    unittest.main()
