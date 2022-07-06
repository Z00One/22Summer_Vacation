# new_id 는 문자열로 입력됨
def solution(new_id):

    # 문자열의 대문자를 소문자로 바꿔준다. ->lower 사용
    new_id = new_id.lower()
    id_list = []

    for value in new_id:
        # 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
        if value.islower() or value.isdigit() or value == "-" or value == "_" or value == ".":
            id_list.append(value)
    
    # 마침표(.)가 2번 이상 연속된 부분 특정
    for index in range(len(id_list) - 1):
        comma_count = 0
        # . 나오는 순간부터 점 카운트
        if id_list[index] == ".":
            # 점이 얼마나 연속적인지 카운트
                for check in id_list[index :]:
                    if check == ".":
                        comma_count+=1
                    else:
                        break
                # 연속적인 점의 갯수가 2개 이상이면
                if comma_count >=2:
                    for change in range(index+1,index+comma_count):
                        # 처음 나온 . 말고 다른 인덱스들의 값을 바꿔준다.
                        id_list[change] = "#"
                    
    # 특정 값들을 빼고 id_list를 다시 구성한다.
    id_list = [ele for ele in id_list if ele!="#"]

    # 마침표(.)가 처음이나 끝에 위치한다면 제거
    if len(id_list)>=1 and id_list[0]==".": 
        del id_list[0]
    # 마지막에 오는 값 확인
    if len(id_list)>=1 and id_list[-1]==".": 
        del id_list[-1]

    # 빈 문자열이라면, new_id에 "a"를 대입
    if len(id_list) == 0 : id_list.append("a")

    # 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
    if len(id_list) >= 15 : 
        del id_list[15:]
        # 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거
        if id_list[0]==".":
            del id_list[0]
        
        if id_list[-1] == ".": # 마지막에 오는 값 확인
            del id_list[-1]

    # 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙임
    while len(id_list) < 3:
        id_list.append(id_list[-1])
    
    # 리스트를 문자열로 변환
    answer = ''.join(id for id in id_list)
    return answer
