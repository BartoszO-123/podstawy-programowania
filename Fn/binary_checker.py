def f(binary_number):
    """Sprawdza, czy ciąg znaków jest prawidłową liczbą binarną (zawiera tylko '0' i '1')."""
    for char in binary_number:
        if char not in '01':
            return False
    return True