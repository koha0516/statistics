import pandas as pd
import numpy as np

"""
このファイルには独自で定義した関数を記述
"""

# 独自の四捨五入関数
def my_round(num, dp=0):
    p = 10**dp
    return (num * p * 2 + 1) // 2 / p

