import math
from util import my_round

"""
このプログラムはベルヌーイ試行(二項実験)に関して、確率分布、二項分布の平均、二項分布の分散を求めるプログラムです。
pはある一方が起こる確率
nは試行回数
"""
p = 1/3
numerator = 1   # 分子
denominator = 3 # 分母

n = 5

# p = 1/4
# numerator = 1   # 分子
# denominator = 4 # 分母
#
# n = 6

dp = 2      # 小数点以下何位まで求めるか
# ==============================================================================


# 確率変数を求める
X = list(range(0, n + 1))
print(X)

for i in X:
    print(f'X={i}のとき')
    print(math.comb(n, i) * (numerator ** i) * (denominator - numerator) ** (n - i))
    print('------')
    print(denominator ** n)
    print('')


# 期待値を求める
total = 0
for i in X:
    ex = math.comb(n, i) * (p ** i) * ((1 - p) ** (n - i)) * i
    total += ex

print('期待値E(X)は次の通り')
print(my_round(total, dp))
print('')


# 確率分布の分散を求める
print('確率分布の分散(二項分布)は')
print(my_round(n * p * (1 - p), 2))
print('')

# ==============================================================================
# ポアソン分布のとき、確率変数X=xである確率を求める
p = 0.002
n = 1000
x = 0

px = (n*p) ** x / math.factorial(x) / (math.e ** (n*p))

print('ポアソン分布においてP(X)は')
print(my_round(px, dp))