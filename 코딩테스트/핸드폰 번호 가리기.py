# 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수
def solution(phone_number):
    # 전화번호 뒷자리 4자리를 제외한 나머지는 "*"로 대체한다
    return "*"*(len(phone_number)-4)   +   phone_number[-4:]
print(solution("2222"))