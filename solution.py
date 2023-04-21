import pandas as pd
import numpy as np


chat_id = 277537153 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    x = np.sort(x)
    med = np.median(x)
    d =float(9*(med**2) -6*med + 1 + 0.24)
    d = np.sqrt(d)
    lam = (3*med - 1 + d) / 264
    return lam # Ваш отве
