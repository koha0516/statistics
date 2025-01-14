import statistics
from util import my_round

"""
このファイルには母分散と母標準偏差の区間推定を行うプログラムが記述されている
"""

# 母分散パターン1 母標平均μが既知の場合の区間推定
data = [
    170, 157, 155, 163, 172, 160, 158, 171, 167, 165,
    172, 163, 178, 165, 185
]

avg = 165.5 # 母平均
n = 15  # 要素数
Xu = 25.00 #カイ二乗の上方信頼限界
Xl = 7.26   #カイ二乗の下方信頼限界

dp=2
# ==============================================================================
wa = 0      # 平均との差の2乗の和
for d in data:
    wa += (d - avg) ** 2

print(wa)
print('信頼区間は以下の通りである。')
print('[' + str(my_round(wa / Xu , dp)) + ',' + str(my_round(wa / Xl , dp)) + ']')
print('')

print('注意！！母平均が未知の場合はXu と Xl の求め方が変わる')


# 母分散･母標準偏差パターン1 母標平均μが既知の場合の区間推定
# 計算があまり複雑ではないので電卓で対応


# ==============================================================================
# パターン2母平均が未知の場合

avg = 166.73 # 標本平均
n = 15  # 要素数
s2 = 66.64  # 不偏分散
Xu = 31.32 #カイ二乗の上方信頼限界
Xl = 4.07   #カイ二乗の下方信頼限界


m = n-1

print('母平均が未知の場合')
print('[' + str(my_round((n-1) * s2 / Xu , dp)) + ',' + str(my_round((n - 1) * s2 / Xl , dp)) + ']')
