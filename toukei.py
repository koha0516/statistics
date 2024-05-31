import math
import statistics


a = [
    170, 157, 155, 170, 163, 172, 160, 158, 171, 167,
    165, 172, 163, 178, 165, 185, 165, 163, 166, 169,
    168, 163, 171, 164, 162, 166, 167, 158, 180, 165
]


# 157, 158, 160, 163, 164, 166, 168, 172

print('配列の中身を昇順に並べると')
array = sorted(a)
print(array)
print('')

N = len(array)

print('四分位数について')
if len(array) % 4 == 0:
    i = N//4
    j = math.floor(N * (3 / 4))
    q1 = (array[i-1] + array[i]) / 2
    q3 = (array[j-1] + array[j]) / 2
else:
    i = N // 4
    j = math.floor(N * 0.75)
    q1 = array[i]
    q3 = array[j]
print(f'第一四分位数は{q1}、第三四分位数は{q3}')
print('')


print('スタージェスの公式より、要素数' + str(N) + 'のとき階級数は')
m = 1 + 3.32 + (math.log10(N))
print(m)
print('切り上げて')
m = math.ceil(m)
print(m)
print('')

print(f'最大値{str(max(array))}、最小値{str(min(array))}、階級数{m}より階級幅は')
c = (max(array) - min(array)) / m
print(c)
print('')

x = c  # ここには自分で決めた階級幅が入ります。
print(f'配列の要素を階級幅{x}ずつ区切ると')
for i in range(m+1): # 一応階級数+1だけ繰り返す
    ar = list()
    for element in array:
        # 〇〇以上、かつ、〇〇未満
        if  element >= min(array) + i * x and element < min(array) + (i+1) * x:
            ar.append(element)
    print(f'{min(array) + i * x}以上、{min(array) + (i+1) * x}未満は{ar}、度数は{len(ar)}、相対度数は{len(ar) / N}')
print('')

print('平均値は')
average = sum(array) / N
print(average)
print('')

print('度数分布表を参考にしない場合の最頻値は')
print(statistics.multimode(array))
print('')

if N % 2 == 1:
    median = array[N // 2]
else:
    median = (array[N // 2 - 1] + array[N // 2]) / 2
print(f'中央値は{median}')
print('')

print('分散は')
print(statistics.pvariance(array))
print('')

print('標準偏差は')
print(math.sqrt(statistics.pvariance(array)))
print('')


# 場合の数全パターンを出す
array1 = ['豚肉', '鶏肉', '牛肉']
array2 = ['焼く', '煮る']
array3 = ['塩', '味噌', '醤油', 'ソース']

for i in array1:
    for j in array2:
        for k in array3:
            print(i, j, k)

