'''
##함수 정의 부분
def plus( v1, v2) :
    result=0
    result=v1+v2
    return result

##변수 선언 부분
hap=0

##메인 코드 부분
while True: 
    a= int(input("더할 수를 입력해주세요 : "))
    b= int(input("더할 수를 입력해주세요 : "))
    hap=plus(a,b)
           
    print("%d와  %d의 plus() 함수 결과는 %d" %(a,b,hap))
'''


'''
##함수 정의 부분
def calc(v1, v2, op):
    result=0
    if op == '+':
        result= v1+v2
    elif op =='-':
        result = v1-v2
    elif op =='*':
        result= v1*v2
    elif op == '/':
        result= v1/ v2

    return result

##변수 선언 부분
res=0
var1, var2, oper=0, 0, ""

##메인 코드 부분
oper=input("계산 입력 (+, -, *, / ): ")
var1=int(input("첫 번째 숫자 입력 : "))
var2=int(input("두 번째 숫자 입력 : "))

res=calc(var1, var2, oper)

print("## 계산기: %d %s %d = %d" %(var1, oper, var2, res))
'''


'''
## 함수 정의 부분
def func1():
    ## global a 입력 시: a가 전역변수로 바뀜
    a=10  #지역변수
    print("func1()에서 a의 값 %d" %a)

def func2():
    print("func2()에서 a의 값 %d" %a)

##변수 선언 부분
a=20  #전역변수

##메인코드 부분
func1()
func2()

'''

'''
##함수 정의 부분
def func1():
    result=100
    return result

def func2():
    print("반환값 없는 함수 실행")

##변수 선언 부분
hap=0

##메인 코드 부분
hap=func1()
print("func1()에서 돌려준 값 ==> %d" %hap)
func2()

'''

'''
##함수 정의 부분
def para2_func(v1, v2):
    result= 0
    result= v1+v2
    return result

def para3_func(v1, v2, v3):
    result= 0
    result= v1+v2+v3
    return result

##변수 선언 부분
hap=0

##메인 코드 부분
hap=para2_func(10, 20)
print("매개변수 2개 함수 호출 결과 ==> %d"%hap)
hap=para3_func(10, 20, 30)
print("매개변수 3개 함수 호출 결과 ==> %d"%hap)
'''

'''
##함수 정의 부분
def para_func(v1, v2, v3=0):
    result= 0
    result= v1+v2+v3
    return result


##변수 선언 부분
hap=0

##메인 코드 부분
hap=para_func(10, 20)
print("매개변수 2개 함수 호출 결과 ==> %d"%hap)
hap=para_func(10, 20, 30)
print("매개변수 3개 함수 호출 결과 ==> %d"%hap)
'''

'''
##함수 정의 부분
def para_func(*para):
    print(type(para))
    result=0
    for num in para:
        result=result+num

    return result

##변수 선언 부분
hap=0

##메인 코드 부분
hap=para_func(10, 20)
print("매개변수 2개 함수 호출 결과 ==> %d" %hap)
hap=para_func(10,20,30)
print("매개변수 3개 함수 호출 결과 ==> %d" %hap)
'''

'''
##딕셔너리 형식의 매개 변수

def dic_func(**para):
    print(type(para)) #para 타입 출력
    print(para)       #para 전체 출력
    print(para.keys()) #para.keys()의 전체 출력
    for k in para.keys():
        print("%s --> %d 명 입니다." %(k, para[k]))

dic_func(아이오아이=11, 소녀시대=8, 걸스데이=4, AOA=7)
'''






