import statistics
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

# 独自のモジュール
from util import my_round

"""
このファイルには統計学の基本的な値を算出するためのプログラムが記述されています
"""
# 1. データをリストに格納する
d = np.array([
    4, 1, 3, 2, 6, 8, 6, 3, 1, 2
])
# 170, 157, 155, 170, 163, 172, 160, 158, 171, 167,
#     165, 172, 163, 178, 165, 185, 165, 163, 166, 169,
#     168, 163, 171, 164, 162, 166, 167, 158, 180, 165,

# 8.5, 7.8, 7.2, 9.0, 8.2, 8.5, 7.9, 7.5, 8.5, 7.2
# 8.1, 7.5, 6.7, 8.0, 7.3, 8.0, 6.8, 7.0, 8.0, 7.7

dp = 2      # 小数点以下何位まで求めるか
# ==============================================================================


print('元データ')
print(d)
print('')


# 2. データを昇順に並べ替える
data_nd = np.sort(d)

print('ソート済みデータ')
print(data_nd)
print('')


data_list = data_nd.tolist()       # データをリスト化する
data_series = pd.Series(data_list)      # データをシリーズ化する


# 要素数
N = len(data_nd)

print('要素数N は')
print('N=' + str(N))
print('')


# 3. 階級数の決定
m = 1 + 3.32 + (math.log10(N))
ceil_m = math.ceil(m)

print(f'スタージェスの公式より、要素数{str(N)}のとき、階級数m は')
print('m=' + str(m))
print('よって、小数点以下を切り上げて')
print('m=' + str(ceil_m))
print('')

# 階級幅の決定
max = np.max(data_nd)
min = np.min(data_nd)
c = (max - min) / ceil_m
c = my_round(c, dp)

print(f'階級幅は小数点以下第{dp}位まで求める。')
print(f'最大値{str(max)}、最小値{str(min)}、階級数{ceil_m} より階級幅c は')
print('c=' + str(c))
print('')


# 度数分布表を表示

total1 = 0
total2 = 0
se_array = list()
cols = pd.Series(['階級', '度数', '相対度数', '累積度数', '累積相対度数'])
se_array.append(cols)
for i in range(ceil_m+1): # 階級数は+1しておく
    ar = list()
    for element in data_list:
        # 〇〇以上、かつ、〇〇未満
        if  element >= min + i * c and element < min + (i+1) * c:
            ar.append(element)

    total1 += len(ar)
    total2 += my_round(len(ar) / N, dp)
    new_series = pd.Series([f'{min + i * c}以上、{min + (i+1) * c}未満', len(ar), my_round(len(ar) / N, dp), total1, total2], name=(i + 1))

    se_array.append(new_series.to_frame())

# Seriesを結合してデータフレームを作成
df = pd.concat(se_array, axis=1)

# 1列目の値をインデックスに設定する
df.set_index(0, inplace=True)

# 行と列を入れ替える
new_df = df.T

print(f'階級幅{str(c)}より、度数分布表は次の通り')
print(new_df)
print('')

# ============ヒストグラムの描画==============
# 日本語を表示できるようにフォントを設定（Windows環境）
plt.rcParams["font.family"] = "Yu Gothic"

# gridの線がグラフより背面になるように設定
plt.rcParams["axes.axisbelow"] = True

# 階級の幅が3になるように指定
plt.hist(x=data_nd, bins=(ceil_m + 1), range=[float(min), float(max + c)], color='lightblue', edgecolor="black")

# 横軸の目盛りを指定
plt.xticks(np.arange(min * (10 * dp), max * (10 * dp) + c * 2 * (10 * dp), c * (10 * dp)) / (10 * dp))

# 縦軸の範囲を指定
max_n = new_df['度数'].max()
plt.ylim(0, max_n + 2)
# gridの横線を追加
plt.grid(axis="y")

plt.title("タイトル")
plt.xlabel("横軸ラベル")
plt.ylabel("縦軸ラベル")


# =========代表値の算出===========
# 最頻値の算出
print('最頻値は')
print(statistics.multimode(data_list))
print('')


# 中央値の算出
print('中央値は')
print(statistics.median_low(data_list))
print(statistics.median_high(data_list))
print(statistics.median(data_list))
print('')


# 四分位数の算出
if len(data_list) % 4 == 0:
    i = N//4
    j = math.floor(N * (3 / 4))
    q1 = (data_list[i-1] + data_list[i]) / 2
    q3 = (data_list[j-1] + data_list[j]) / 2
else:
    i = N // 4
    j = math.floor(N * (3 / 4))
    q1 = data_list[i]
    q3 = data_list[j]
print(f'第一四分位数は{q1}、第三四分位数は{q3}')
print('')


# 平均値の算出
mean = statistics.mean(data_list)
print('平均値は')
print(mean)
print('')


# 分散の算出
variance = statistics.pvariance(data=data_list, mu=mean)
print('分散は')
print(my_round(variance, dp))
print('')


# 標準偏差の算出
sd = statistics.pstdev(data=data_list, mu=mean)
print('標準偏差は')
print(my_round(sd, dp))
print('')

print('標本平均の分散を求めている場合は、元の分散をnで割る')
print('標本分散の期待値v^2 は、元の分散σ^2 の(n-1) / n 倍')
print('不偏分散の期待値s^2は、標本分散の期待値v^2の n / (n-1)倍')
