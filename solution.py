import pandas as pd
import numpy as np


chat_id = 146155552 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    t = 76
    n = len(x)
    lmbd = x.sum() / (t*n)
    return lmbd
