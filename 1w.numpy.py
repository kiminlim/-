#!/usr/bin/env python
# coding: utf-8

# # 1.5 넘파이
# 
# * 넘파이를 쓰는 이유:
# 
# 파이썬은 c++보다 계산속도가 느려서, c로 계산해서 파이썬으로 불러오는 넘파이 라이브러리를 씀!!

import numpy as np


# 넘파이 배열 생성하기
x = np.array([1.0, 2.0, 3.0])
print(x)
type(x) # 파이썬 list 객체를 개선한 넘파이의 ndarray는 객체

# 넘파이의 산술 연산
x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])
print(x + y) # 원소별 덧셈
print(x - y) # 원소별 뺄셈
print(x * y) # 원소별 곱셈
print(x / y) # 나눗셈
print(y / x)
print(y // x) # 몫
print(y % x) #?
x / 1



# 넘파이의 n차원 배열
# : 넘파이에서는 다차원 배열도 가능

A = np.array([[1.0,2.0],[3,4]])
print(A)
print(A.shape)
A.dtype # 행렬의 자료형을 알려줌
# int32 는 그냥 정수형이라 생각하면 됨, 32비트가 할당된 숫자라는 의미! (실수는 64비트 할당.)


# 행렬 연산
B = np.array([[3,4],[5,6]])
print(A + B) 
print(A * B) 
print(A / B)
A * 10


#  1차원배열 : 벡터
#  2차원배열 : 행렬
#  3차원 이상의 배열 : 다차원 배열
# 


# 브로드캐스트
# 란 행렬은 확장해서 계산해주는 넘파이의 기능
#A = np.array([[1,2],[3,4]])
A = np.array([[1,2],[3,4],[5,6]])
B = np.array([10,20])
A * B


# 원소 접근
X = np.array([[51,55],[14,9],[0,4]])
print(X)
print(X[1]) # 1행
X[1][1] # (1,1) 1행1열의 원소



# 포문으로 각 원소 불러오기
for row in X:
    print(X)
    


X = X.flatten() # X를 1차원 배열로 변환해줌
print(X)

X[np.array([0,1,2])] # 0,1,2 인덱싱 



X > 15
X[X>15] # 15보다 큰 것만 가져와




