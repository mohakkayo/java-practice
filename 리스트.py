#리스트

'''
##소스코드7-2

aa=[0, 0, 0, 0]
hap=0

aa[0]=int(input("1 번째 숫자: "))
aa[1]=int(input("2 번째 숫자: "))
aa[2]=int(input("3 번째 숫자: "))
aa[3]=int(input("4 번째 숫자: "))

hap=aa[0]+aa[1]+aa[2]+aa[3]

print("합계 ==> %d " %hap)
'''
'''
##소스코드7-3
aa=[]
for i in range(0, 4):
    aa.append(0)
hap=0

for i in range(0,4):
    aa[i]=int(input( str(i+1) + "번째 숫자 : "))

hap=aa[0]+aa[1]+aa[2]+aa[3]

print("합계 ==> %d" %hap)
'''

'''
##소스코드 7-4
aa=[]
bb=[]
value=0

for i in range(0, 100):
    aa.append(value)
    value+= 2

for i in range(0, 100):
    bb.append(aa[99-i])

print("bb[0]은 %d, bb[99]는 %d 입력됨 " %(bb[0], bb[99]))
'''


##num=[1,8,7,


'''
v=[1, 8, 7,3,2,10,41,6,5, 100, 12]
print(max(v))
print(min(v))


'''

b=[]
for i in range(7):
    a=int(input("7가지 숫자를 입력하세요(%d회): " %(i+1)))

    b.append(a)
    b=list(set(b))

print(b)
print("최대 값은 %d" %max(b))
print("최소 값은 %d" %min(b))










      
