import random as r

# sort 함수 정의
def sort(list_value, min_value, max_value):
    new_list = []
    for index_value in range(min_value, max_value + 1):
        # 제일 작은 수부터 제일 큰 수까지 입력된 리스트에 있다면
        while index_value in list_value:
            # 해당 리스트에서 빼주고
            list_value.remove(index_value)
            # 새로운 리스트에 추가한다.
            new_list.append(index_value)
    return new_list

#  1 ~ 20 사이 양의 정수 중 난수 값 20개 생성 후 List에 저장
List = [r.randint(1,20) for element in range(20)]
histogram_value = [0,0,0,0]

# 히스토그램 값 정하기
for element in List:
    if element<=5:
        histogram_value[0] += 1
    elif element<=10:
        histogram_value[1] += 1
    elif element<=15:
        histogram_value[2] += 1
    else:
        histogram_value[3] += 1

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

#  List 내 원소 값에 대한 합계, 평균, 최대 값, 최소 값 구하기
sum = 0
minimum_value = 20
maximum = 0
for element in List:
    # List 안의 요소들을 더해준다
    sum += element
    # element 값을 계속 비교하면서 최소값 최대값 설정
    if element < minimum_value: # 최소
        minimum_value = element
    if element > maximum: # 최대
        maximum = element
# 평균 --> 합계를 원소 갯수로 나누기
avg = sum / len(List)

# 합계, 평균, 최대 값, 최소 값 출력 하기
print("최소 값 :", minimum_value)
print("최대 값 :", maximum)
print("합계 :", sum)
print("평균 :", avg)

# 작은 값부터 나열하기
List = sort(List, minimum_value, maximum)

print("중복 값","    ","중복 횟수")
for element in List:
# 중복 값과 중복 횟수 정하기
    element_count = 0
    # 어떤 값이 중복 되는지 정하기
    for count in List:
        # 얼마나 중복되는지 정하기
        if element == count:
            element_count += 1
    if element_count >= 2:
        # 중복된 값들을 빼주기 -- > 중복 값에 다시 나올 수도 있다.
        while element in List:
            List.remove(element)
        # 중복됐다면 값을 출력
        print(" ",element,"\t\t",element_count)

#  구간 별 히스토그램 정보 출력
print("구간별 히스토그램")
print("  1 ~ 5 :","*"*histogram_value[0])
print(" 6 ~ 10 :","*"*histogram_value[1])
print("11 ~ 15 :","*"*histogram_value[2])
print("16 ~ 20 :","*"*histogram_value[3])