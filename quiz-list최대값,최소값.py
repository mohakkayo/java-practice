##1020-list 최대값 최소값 구하기


'''
## 1
v=[1, 8, 7,3,2,10,41,6,5, 100, 12]
print(max(v))
print(min(v))


'''
'''
# 2

b=[]
for i in range(7):
    a=int(input("7가지 숫자를 입력하세요(%d회): " %(i+1)))

    b.append(a)
    b=list(set(b))

print(b)
print("최대 값은 %d" %max(b))
print("최소 값은 %d" %min(b))
'''
