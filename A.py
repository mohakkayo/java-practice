'''
import Func

##메인코드 부분
Func.func1()
Func.func2()
Func.func3()

'''
'''
##from 모듈명 import 함수1, 2, 3
##from 모듈명 import*
from Func import func1, func2, func3

func1()
func2()
func3()
'''

'''
from Func import*

func1()
func2()
func3()
'''
'''
import sys
print(sus.builtin_module_names)

'''
'''
from myCalc import *

##메인코드부분

in1=float(input("첫 번째 숫자를 입력하세요 : "))
op=input("연산자(+, -, *, /)를 입력하세요 : ")
in2=float(input("두 번째 숫자를 입력하세요 : "))

print()
print("*** 모듈로 작성한 계산기 호출 결과 ***")
if op == '+' :
    print("%5.1f + %5.1f = %5.1f" % (in1, in2, plus(in1, in2)))
elif op=='-':
    print("%5.1f - %5.1f = %5.1f" % (in1, in2, minus(in1, in2)))
          
elif op=='*':
    print("%5.1f - %5.1f = %5.1f" % (in1, in2, multiply(in1, in2)))
elif op=='/':
    print("%5.1f - %5.1f = %5.1f" % (in1, in2, divide(in1, in2)))

else :
    print("연산자를 모르겠네요 ! ")


'''





    
    
    
