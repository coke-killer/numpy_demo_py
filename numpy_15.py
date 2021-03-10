# __author__: "yudongyue"
# date: 2021/3/9
import numpy as np

print('数组的拆分与合并')
x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([[7, 8, 9], [10, 11, 12]])
print(np.concatenate([x, y], axis=0))  # 竖直组合
print(np.concatenate([x, y], axis=1))  # 水平组合
print('垂直stack 与水平stack')
print(np.vstack((x, y)))
print(np.hstack((x, y)))
# dstack: 按深度堆叠
print(np.split(x, 2, axis=0))  # 按行分割 [array([[1, 2, 3]]), array([[4, 5, 6]])]
print(np.split(x, 3, axis=1))  # 按列分割
# 堆叠辅助类
arr = np.arange(6)
arr1 = arr.reshape((3, 2))
arr2 = np.random.randn(3, 2)
print('r_用于按行堆叠')
print(np.r_[arr1, arr2])
print('c_用于按列堆叠')
print(np.c_[np.r_[arr1, arr2], arr])
print('切片直接转为数组')
print(np.c_[1:6, -10:-5])
