def solution(price, money, count):
    #입출력 예
    # 이용금액이 3인 놀이기구를 4번 타고 싶은 고객이 현재 가진 금액이 20이라면,
    # 총 필요한 놀이기구의 이용 금액은 30 (= 3+6+9+12) 이 되어 10만큼 부족하므로 10을 return 합니다.

    for value in range(1, count + 1):   # 돈이 부족한 지 충분한 지 판별
        money -= price * value

    answer = -money if money < 0 else 0 # 돈이 부족하면 부족한 만큼 절댓값 set, 돈이 충분하다면 0 set

    return answer