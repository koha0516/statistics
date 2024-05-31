import statistics
from util import my_round

"""
このファイルには標本分布に関する計算を行うプログラムが記述されている
"""

data = [
    5, 2, 5, 2, 5, 2, 4, 3, 3, 2
    ]

dp = 2
#===============================================================================


# 標本平均
print('標本平均は')
print(my_round(statistics.mean(data), dp))
print('')

print('分散は')
print(my_round(statistics.pvariance(data), dp))
print('')

print('不偏分散は')
print(my_round(statistics.variance(data), dp))
print('')


