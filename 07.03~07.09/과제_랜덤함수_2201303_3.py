import random

# sort 함수 정의
# sort 함수 정의
def sort(list_value):
    # 비교할 요소 정하기, 마지막에는 결국 제일 큰값이 올 것이기 때문에 마지막 index에서는 반복하지 않는다.
    for index in range(len(list_value)-1):
        # 비교할 요소 다음 index의 요소들 비교하기
        for compare_index in range(index+1,len(list_value)):
            # 만약 자기보다 작은 값이 나온다면
            if list_value[index] > list_value[compare_index]:
                # 자리 바꿔주기
                compare_value = list_value[compare_index] # 변수에 작은 값을 담아준다.
                list_value[compare_index] = list_value[index] # 작은 값이 있던 index의 요소를 큰 값으로 바꿔준다.
                list_value[index] = compare_value # 큰 값이 있던 index의 요소를 작은 값으로 바꿔준다.
    return list_value

#  1 ~ 20 사이 양의 정수 중 난수 값 20개 생성 후 List에 저장
List = [random.randint(1,20) for element in range(20)]

# 요소 값 입력
print("랜덤 값 :")
for index in range(len(List)):
    # 첫번째 값과 중간 값일 때 출력 방식
    if index == 0 or index == len(List)//2:
        print("\t",List[index],end=" ")
    # 중간값 바로 전의 값과 마지막 값에서 줄을 바꿔준다.
    elif index == len(List)//2 - 1 or index == len(List)- 1:
        print(List[index])
    # 나머지 값에서의 처리
    else:
        print(List[index],end=" ")

# 작은 값부터 정렬하기
List = sort(List)

#  List 내 원소 값에 대한 합계, 평균, 최대 값, 최소 값, 히스토그램 중복 값 구하기
sum = 0
histogram_value = [0,0,0,0]
overlap_value = {}
for element in List:
    # List 안의 요소들을 더해준다
    sum += element
    # 히스토그램 값 정하기
    if element<=5:
        histogram_value[0] += 1
    elif element<=10:
        histogram_value[1] += 1
    elif element<=15:
        histogram_value[2] += 1
    else:
        histogram_value[3] += 1
    # 중복 값 정하기
    if element not in overlap_value:
        overlap_value[element] = 1
    else:
        overlap_value[element] += 1

# 평균 --> 합계를 원소 갯수로 나누기
avg = sum / len(List)

# 합계, 평균, 최대 값, 최소 값 출력 하기
print("최소 값 :", List[0])
print("최대 값 :", List[-1])
print("합계 \t:", sum)
print("평균 \t:", avg)

# 중복 값 출력하기
print("중복 값","    ","중복 횟수")
for key in overlap_value.keys():
    if overlap_value[key] >= 2:
        print(" ",key,"\t\t",overlap_value[key])

#  구간 별 히스토그램 정보 출력
print("구간별 히스토그램")
print(" 1 ~  5 :","*"*histogram_value[0])
print(" 6 ~ 10 :","*"*histogram_value[1])
print("11 ~ 15 :","*"*histogram_value[2])
print("16 ~ 20 :","*"*histogram_value[3])