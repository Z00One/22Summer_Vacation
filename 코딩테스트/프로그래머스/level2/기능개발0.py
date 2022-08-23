# def solution(progresses, speeds):
#     answer = []

#     while progresses:
        
#         dayValue = (100 - progresses[0]) // speeds[0]
        
#         progresses = [progresses[index] + dayValue * speeds[index] for index in range(len(progresses))]
        
#         count = 0
        
#         for index in range(len(progresses)):
#             if progresses[index] < 100:
#                 break
#             count +=1

#         progresses = progresses[index :] if len(progresses) > 2 else 0
#         speeds     = speeds[index :]

#         if count:
#             answer.append(count)            

#     return answer

#####
# def solution(progresses, speeds):
#     answer = []
        
#     dayValue = (100 - progresses[0]) // speeds[0]

#     progresses = [progresses[index] + dayValue * speeds[index] for index in range(len(progresses))]

#     count = 0

#     for index in range(len(progresses)):
#         if progresses[index] < 100:
#             break
#         count +=1

#     if count:
#         answer.append(count)
#         if count == len(progresses):
#             return answer
#         return answer + solution(progresses[index :], speeds[index :])


####
def solution(progresses, speeds):
    answer = []

    progresses = [(100 - progresses[index]) // speeds[index] for index in range(len(progresses))]

    for index in 

    return answer
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))