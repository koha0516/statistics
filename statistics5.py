import numpy as np
from util import my_round

"""
このプログラムは確率分布の平均(確率変数の期待値)と確率分布の分散を求めるプログラムです。
"""

odds_list = [1/36, 1/36, 1/18, 1/18, 1/12, 1/12, 1/9, 1/9, 5/36, 5/36, 1/6]
value_list = [2, 12, 3, 11, 4, 10, 5, 9, 6, 8, 7]
# [1/36, 1/36, 1/18, 1/18, 1/12, 1/12, 1/9, 1/9, 5/36, 5/36, 1/6]
# [2, 12, 3, 11, 4, 10, 5, 9, 6, 8, 7]

# [3/70, 7/70, 35/70, 15/70, 10/70]
# [1, 2, 3, 4, 5]

dp = 2      # 小数点以下何位まで求めるか
# ==============================================================================



# 確率分布の平均(期待値のこと)を求める
def calc_expected_value(odds_list, value_list):
    o = np.array(odds_list)
    v = np.array(value_list)
    return(o * v)

expected_value = my_round(sum(calc_expected_value(odds_list, value_list)), dp)       # 小数点第◯位まで求める
print('確率変数の平均は')
print('E(X) = μ =' + str(expected_value))
print('')


# 確率分布の分散を求める
def calc_expected_value2(odds_list, value_list):
    o = np.array(odds_list)
    v = np.array(value_list)
    return(o * v * v)

expected_value2 = my_round(sum(calc_expected_value2(odds_list, value_list)), dp)
variance = my_round(expected_value2 - expected_value * expected_value, dp)
print('確率変数の分散V(X)について V(X)=E(X^2)-μ^2 であるから、')
print('E(X^2) - μ^2 =' + str(expected_value2) + '-' + str(expected_value * expected_value))
print('V(X)=' + str(variance))