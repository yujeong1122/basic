import re

def validate_password(password):
    # 정규 표현식 패턴: 소문자, 대문자, 숫자, 기호가 모두 포함되어야 함
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+=[\]{}|;:",<>\./?])'

    if re.match(pattern, password):
        return "비밀번호가 유효합니다."
    else:
        return "비밀번호는 최소 하나의 소문자, 대문자, 숫자 및 기호를 포함해야 합니다."

# 예시 사용
password = input("비밀번호를 입력하세요: ")
print(validate_password(password))
