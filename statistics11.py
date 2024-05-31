import math
from util import my_round

"""
このファイルには母比率の区間推定の計算プログラムが記述してある
"""

n = 20      # 試行回数
X = 11      # どちらか一方の事象が起こった回数
z = 2.575  # 標準正規化変数

dp = 2
#=======================================================================
temp = X / n

U = temp - (z * math.sqrt((temp * (1 - temp)) / n))
L = temp + (z * math.sqrt((temp * (1 - temp)) / n))

# 母比率の信頼区間
print('母比率の信頼区間は以下の通り')
print('[' + str(my_round(U, dp)) + ',' + str(my_round(L, dp)) + ']')