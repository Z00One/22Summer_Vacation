# new_id 는 문자열로 입력됨
def solution(new_id):

    # 문자열의 대문자를 소문자로 바꿔준다. ->lower 사용
    new_id = new_id.lower()
    id_list = []
    # for문을 돌려서 빼면 효율이 떨어질 듯
    for value in new_id:
        # 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
        if value.islower() or value.isdigit() or value == "-" or value == "_" or value == ".":
            id_list.append(value)
    
    # 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    # 문자열을 리스트화 하고 연속된 . 이 있다면 제거
    
    # 인덱스를 하나씩 확인한다.
    comma_count = 0
    index = 0
    flag = True
    while flag:
        # index 가 id_list의 범위를 넘어가는 순간 
        if index >= len(id_list):
            flag = False

        elif id_list[index] == ".":
            comma_count += 1
            if len(id_list) < 2 or len(id_list) < index:
                flag = False
            elif id_list[index - 1] ==      "." and comma_count >=2:
                for comma in range(index-comma_count + 2, index + 1):
                    id_list[comma] = "#"
                    # 연속되는 값이 없다면 comma_count 리셋
                    flag = False
            elif id_list[index+1] != "." and comma_count >=2:
                for comma in range(index-comma_count + 2, index + 1):
                    id_list[comma] = "#"
                # 연속되는 값이 없다면 comma_count 리셋
                comma_count = 0
            # 다음 인덱스의 값이 . 이 아니고 3번 이상 카운트 됐을 경우

            # 다음 인덱스의 값이 . 이 아니고 3번 미만으로 카운트 됐을 경우
            elif id_list[index+1] != "." and comma_count <2:
                # 연속되는 값이 없다면 comma_count 리셋
                comma_count = 0
        # 연속해서
        else:
            comma_count = 0
        index += 1
    id_list = [ele for ele in id_list if ele != "#"]
    # 마침표(.)가 처음이나 끝에 위치한다면 제거
    while not flag:
        if len(id_list) == 0:
            flag =True
        elif id_list[0] == ".": # 처음에 오는 값 확인
            del id_list[0]
        elif id_list[-1] == ".": # 마지막에 오는 값 확인
            del id_list[-1]
        # 처음이나 끝에 "."이 없을 때까지 반복
        else:
            flag = True
    
    # 빈 문자열이라면, new_id에 "a"를 대입
    if len(id_list) == 0 : id_list.append("a")

    # 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
    elif len(id_list) >= 15 : 
        del id_list[15:]
        # 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거
        if id_list[-1]==".":
            flag = True
            while flag:
                if id_list[-1] == ".": # 마지막에 오는 값 확인
                    del id_list[-1]
                # 처음이나 끝에 "."이 없을 때까지 반복
                else:
                    flag=False

    # 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙임
    if len(id_list) <= 2:
        while len(id_list) < 3:
            id_list.append(id_list[-1])
    
    # 리스트를 문자열로 변환
    answer = ''.join(id for id in id_list)
    return answer

print(solution("z-+.^."))