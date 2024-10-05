import math
# 덧셈함수
def cus_sum(a, b):
    return a + b
#뺄셈함수
def cus_sub(a, b):
    return a - b
#곱셈함수
def cus_mul(a, b):
    return a * b
#나눗셈함수
def cus_div(a, b):
    if b != 0:
        return a / b
    else:
        return None
#예외처리
def cus_except(a, b):
    return '올바르지 않은 입력입니다.'
#case별 함수 호출을 위한 딕셔너리 맵핑
switch_dict = {
    'sum': cus_sum,
    'sub': cus_sub,
    'mul': cus_mul,
    'div': cus_div
}

#모두 삭제하여 해결

#입력된 연산자를 통해 맵핑된 함수 탐색
def detect_case(value, x, y):
    return switch_dict.get(value, cus_except)(x, y)

# main부 - 입력양식 공지
print("--------------- 입력 양식 ---------------")
print("-- 덧셈: sum a b (and result => a + b)")
print("-- 뺄셈: sub a b (and result => a - b)")
print("-- 곱셈: mul a b (and result => a * b)")
print("-- 나눗셈: div a b (and result => a / b)")
print("-- 종료: exit (and result => shut down)")
while True:
    # 종료조건 탐색
    data = input()
    if data == 'exit':
        break
    # 부족한 입력의 개수에 대한 예외처리
    try:
        op ,x, y = data.split()
    except ValueError:
        print('올바르지 않은 입력입니다.')
        continue
    
    # 정수형 자리의 문자열 입력에 대한 예외처리
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        print('올바르지 않은 입력입니다.')
        continue
    
    print(detect_case(op, x, y))
    