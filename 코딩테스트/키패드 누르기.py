def solution(numbers, hand):
    left       = "*"                # 왼손의 위치
    right      = "#"                # 오른손의 위치
    leftValue  = [1, 4, 7, "*"]     # 왼손만 올릴 수 있는 리스트  
    rightValue = [3, 6, 9, "#"]     # 오른손만 올릴 수 있는 리스트
    midValue   = [2, 5, 8, 0]       # 왼손, 오른손 둘 다 올릴 수 있는 리스트
    answer     = ''                 # 어느 손을 얼마나 움직였는지 담는 변수
    
    for value in numbers:           # 번호 받아서 분류
        if value in leftValue:      # 왼손
            left = value
            answer += 'L'
        
        elif value in rightValue:   # 오른손
            right = value
            answer += 'R'
            
        else:                       # 중간값
            # 세로 차이
            rihgtRow = abs(rightValue.index(right) - midValue.index(value)) if right in rightValue else abs(midValue.index(right) - midValue.index(value))
            leftRow  = abs(leftValue.index(left) - midValue.index(value)) if left in leftValue else abs(midValue.index(left) - midValue.index(value))

            # 가로 차이
            rihgtCol = 0 if right in midValue else 1
            leftCol  = 0 if left in midValue else 1
            
            # 가까운 손
            if rihgtCol + rihgtRow > leftCol + leftRow:
                answer += 'L'
                left = value
                
            elif rihgtCol + rihgtRow < leftCol + leftRow:
                answer += 'R'
                right = value
            
            # 거리가 같다면 손잡이 정보로 선택
            else:
                if hand == 'right':
                    answer += 'R'
                    right = value

                else:
                    answer += "L"
                    left = value
                    
    return answer
#LRLLLRLLRRL          
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],'right'))