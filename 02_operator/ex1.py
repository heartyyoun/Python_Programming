# 연산자

# 산술 연산자
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)  # 나머지
print(a // b)  # 몫
print(a**b)  # 거듭제곱

# 복합 대입 연산자
a += 4
print(a)

# 증감 연산자
# a++ (이건안된답니다 엉ㅠ )
# b = a++
# b = ++a
a += 1

# 비교 연산자
print(3 == 3.0)  # True
print(3 != 4)  # True
print("apple" < "apble")  # False
print(1 < 2 < 3)  # True
print(1 < 3 < 2)  # False

# 논리 연산자 (and, or, not)
print(True and True)  # T
print(True or False)  # T
print(not True)  # F

# Short-circuit 테스트
a = 10
b = 0

# print(a / b)

if a > 0 or a / b:
    print("yes")
else:
    print("no")
