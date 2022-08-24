def solution(progresses, speeds):
    answer = []

    # while progresses:
    #     count = 0
    #     dayValue = (100 - progresses[0]) // speeds[0]
        
    #     for index in range(len(progresses)):
    #         if (progresses[index] + (dayValue * speeds[index])) < 100:
    #             break
    #         count += 1
        
    #     progresses = progresses[index:] if len(progresses) > 2 else []
    #     speeds     = speeds[index:]
                
    #     answer.append(count)
    count = 0
    
    for index in range(len(progresses)):
        if not(count) :
            dayValue = int((100 - progresses[index]) // speeds[index]) + 1

        if (progresses[index] + (dayValue * speeds[index])) < 100:
            answer.append(count)
            dayValue = (100 - progresses[index]) // speeds[index]
            count = 0
        
        count +=1

    answer.append(count)            

    return answer
print(solution([96, 99, 98, 97], [1,1,1,1]))

# 예제 1)[99, 99, 99] ,[1, 1,1]
# progresses : [40, 93, 30, 55, 60, 65]
# speeds : [60, 1, 30, 5 , 10, 7]
# return : [1,2,3]
# [99, 1, 99, 1] [1, 1, 1, 1] [1, 3]
# 예제 2)
# progresses : [93, 30, 55, 60, 40, 65]
# speeds : [1, 30, 5 , 10, 60, 7]
# return : [2,4]