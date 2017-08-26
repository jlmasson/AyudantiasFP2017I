import numpy as np
from random import randint

def colocarMinas(campo, cantidad, orientacion):
    # orientacion:
    # True -> horizontal
    # False -> vertical
    for i in range(1, cantidad + 1):
        f = randint(0, campo.shape[0] - 1)
        c = randint(0, campo.shape[1] - 1)
        if orientacion:
            pedazo = campo[f, c: c + 3]
            while len(pedazo) < 3 and pedazo.sum() != 0:
                f = randint(0, campo.shape[0])
                c = randint(0, campo.shape[1])
                pedazo = campo[f, c: c + 3]
            campo[f, c: c + 3] = i

campo = np.zeros((5, 5), int)
colocarMinas(campo, 5, True)
print(campo)