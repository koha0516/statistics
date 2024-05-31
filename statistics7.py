from scipy.stats import norm
from util import my_round

"""
正規分布に関する計算を行うプログラムです。
微妙に正確じゃないのでうまくやってください。
"""
x = 450000     # 調べたい値
avg = 220000  # 平均
scale = 100000  # 標準偏差
# ==========================================================


res =  norm.sf(x=x, loc=avg, scale=scale)

print('標準正規化変数z は')
print('z=' + str(my_round((x - avg) / scale, 2)))
print('')

print('x以上となる確率(仮)は')
print(my_round(res, 4))

print('x以下となる確率(仮)は')
print(1 - my_round(res, 4))
