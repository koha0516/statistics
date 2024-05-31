import math
from util import my_round
"""
このファイルには2つの母比率の差の検定に関する計算式が入っています
式8.33
"""

na = 400
nb = 300

Xa = 50
Xb = 20

dp=2
# =============================================
temp = (Xa+Xb) / (na+nb)

z = (Xa/na - Xb/nb) / math.sqrt(temp * (1 - temp) * (1/na + 1/nb))

print('中央項は')
print('z = ' + str(my_round(z, 4)))