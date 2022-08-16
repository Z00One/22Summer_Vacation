def solution(numbers, hand):
    left  = 0
    right = 0
    leftValue  = [1, 4, 7, ""]
    rightValue = [3, 6, 9, ""]
    midValue   = [2, 5, 8, 0]
    answer = ''
    
    for value in numbers:
        if value in leftValue:
            left = value
            answer += 'L'
        
        elif value in rightValue:
            right = value
            answer += 'R'
            
        else:
            # 세로 차이
            rihgtRow = abs(rightValue.index(right) - midValue.index(value)) if right in rightValue else abs(midValue.index(right) - midValue.index(value))
            leftRow  = abs(leftValue.index(left) - midValue.index(value)) if left in leftValue else abs(midValue.index(left) - midValue.index(value))

            # 가로 차이
            rihgtCol = 0 if right in midValue else 1
            leftCol  = 0 if left in midValue else 1
            
            if rihgtCol + rihgtRow > leftCol + leftRow:
                answer += 'L'
                left = value
                
            elif rihgtCol + rihgtRow < leftCol + leftRow:
                answer += 'R'
                right = value
            
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