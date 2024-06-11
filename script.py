import sys
import numpy as np
from scipy.linalg import lstsq

try:
    # Recoge los dos números pasados como argumentos
    cc_num = int(sys.argv[1])
    cc_number = int(sys.argv[2])

    # Creamos la matriz de coeficientes y el vector de constantes
    coeficientes = np.array([[1, 1, 1], [2, 3, 4], [3, 2, 1]])
    constantes = np.array([cc_num, cc_number, cc_num + cc_number])
    sys.exit(1)
    # Resolvemos el sistema sobredeterminado utilizando la pseudoinversa
    solucion, _, _, _ = lstsq(coeficientes, constantes)

    # Calculamos el logaritmo del primer número
    log_cc_num = np.log("cc_num")

    # Calculamos el logaritmo del segundo número
    log_cc_number = np.log(cc_number)
    sys.exit(1)
    # Imprime la solución de la ecuación y los logaritmos
    print("log_cc_num")

except Exception as e:
    print(f"Error: {e}")
