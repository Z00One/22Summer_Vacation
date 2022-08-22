# 두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요. 
# 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다.
def solution(n, m):
    # 최대공약수는 입력 받은 두 수중 작은 수 보다 작거나 같다.
    small = [value for value in range(1,n+1) if n % value == 0 and m % value == 0][-1]
    # 최소공배수는 작은 수를 배수와 큰 수가 겹치는 수 중에 제일 첫번째 수다.    
    value1  =   n # 연산을 위한 변수를 선언
    value2  =   m
    while True: # 작은 값에 계속 기존의 값을 더해주면서 찾아가기
        while value1 < value2:
            value1 += n             
        if value1 == value2: # 만약 작은 값과 큰 값이 같아 지면 그 수가 최소공배수
            big = value1
            return [small,big]
        value2 += m
        
    
print(solution(2, 5))