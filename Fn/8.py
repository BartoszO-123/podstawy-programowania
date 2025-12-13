
def m_to_cm(n):
    return n * 100


def cm_to_m(n):
    return n / 100


def cm_to_inches(n):
    return n / 2.54


def feet_and_inches_to_cm(feet, inches):
    total_inches = (feet * 12) + inches
    return total_inches * 2.54


if __name__ == "__main__":
    print(f"2m = {m_to_cm(2)}cm")
    print(f"532cm = {cm_to_m(532)}m")

    print(f"10cm = {cm_to_inches(10):.2f} cali")
    print(f"5 stóp i 10 cali = {feet_and_inches_to_cm(5, 10):.2f}cm")
