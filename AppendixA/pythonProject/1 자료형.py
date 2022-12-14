##### 수 자료형 ######

#1. 정수형 : 양, 음의 정수 와 0이 있다.
print("1. 정수형이란?\n")
a = 1000
b = -50
c = 0
print(a+b+c)

# 2.실수형 : 소수점 아래 데이터를 포함하는 수
# 표현 방법 : 유효숫자 e지수 = 유효숫자x10지수
print("2. 실수형이란?\n")
a = 1e3 # 1000
print(a)
b = 3E5 # e,E 모두 사용 가능
print(b)
c = 3954e-4
print(c)

# 주의: 2진수 체계에서는 소수를 정확하게 표현할 수 있는 방법이 없다.따라서 소수점 값을 비교하는 작업이 필요할 때 실수 값을 비교하지 못하는 문제 발생.
a = 0.3 + 0.6

if a == 0.9:
    print(a)
    print(True)
else:
    print(a)
    print(False)

# round()를 사용하자 ! , round(실수형 데이터 , 반올림하고자하는 위치 -1)

a= round(123.456,2)
print(a)

a = round(0.3+0.6,4)

if a == 0.9:
    print(a)
    print(True)
else:
    print(a)
    print(False)

# 3. 수 자료형의 연산 (+,-,*,/,//,%, **)
print("3. 수 자료형의 연산이란?\n")
a = 7
b = 3
# 나누기 연산자 , 결과를 실수형으로 처리한다.
print(a/b)

#나머지 연산자, 예: 'a가 홀수인지 확인할 때' =>a %2 != 0
print(a%b)

# 몫 연산자 , 나눈 결과에서 몫만을 얻고자할 때 이용
print(a//b)

# 거듭제곱 연산자 , x**y 처럼 사용되는데 여기서 x는 밑,y는 지수를 의미한다.
a = 2
b = 10
print(a**b)

