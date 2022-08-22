# def solution(n, arr1, arr2):

#     for index in range(n):                      # 2진수로 바꾸기
#         num = ''                                # --> 여러가지 함수나 메소드를 사용하면 더 짧게 구현 가능
#         while arr1[index] > 0:
#             num = str(arr1[index] % 2) + num
#             arr1[index] //= 2
#         arr1[index] = num

#         while len(arr1[index]) < n:
#             arr1[index] = '0' + arr1[index]

#         num = ''
#         while arr2[index] > 0:
#             num = str(arr2[index] % 2) + num
#             arr2[index] //= 2
#         arr2[index] = num

#         while len(arr2[index]) < n:
#             arr2[index] = '0' + arr2[index]

#     answer = []

#     for indexA in range(n):                     # '#' 또는 ' ' 로 바꾸기
#         value = ''

#         for indexB in range(n):

#             if arr1[indexA][indexB] == '1' or arr2[indexA][indexB] == '1':
#                 value += '#'

#             else:
#                 value += ' '

#         answer.append(value)
#     return answer


################ 다른 사람 답

def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):            # 각각의 리스트 arr1, arr2 의 원소값 i, j를 한 번에 얻는다.
        print(13|25)                        # 정수에서 합집합 연산을 하면 각각의 자릿수
        a12 = str(bin(i | j)[2 :])          # i, j 를 2진수로 변환한 값의 합집합
        a12 = a12.rjust(n, '0')
        a12 = a12.replace('1', '#')
        a12 = a12.replace('0', ' ')
        answer.append(a12)
    return answer
print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))