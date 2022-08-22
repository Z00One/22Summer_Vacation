# new_id 는 문자열로 입력됨
def solution(new_id):

    # 문자열의 대문자를 소문자로 바꿔준다. ->lower 사용
    new_id.lower()
        
    # 문자열을 리스트화 하고 연속된 . 이 있다면 제거
    mylist = list(new_id)

    # for문을 돌려서 빼면 효율이 떨어질 듯
    for index in range(len(mylist)-1):
        # 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
        if mylist[index].islower() or mylist[index].isdigit() or mylist[index] == "-" or mylist[index] == "_" or mylist[index] == ".":
            pass
        else : 
            mylist[index]="#"
        
    mylist=[ele for ele in mylist if ele != "#"]
    # 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    # 인덱스를 하나씩 확인한다.
    comma_count = 0
    for index in range(len(mylist)-1):
        # 엘리먼트가 . 이 나온 최초의 인덱스a를 저장 및 카운트
        if mylist[index] == ".":
            comma_count += 1
            if comma_count==1:
                a = index

        # 인덱스 값이 .이 아닌 순간에 카운트가 3이 넘는 경우
        elif mylist[index] != "." and comma_count >=2:
            # 해당 인덱스보다 1작은 값을 인덱스b로 저장
            b = index-1
            mylist[a:b] = "#"
            # 카운트 초기화
            comma_count = 0

        # 나머지 카운트 0 으로 초기화 or 0으로 유지
        else:
            comma_count = 0
    mylist=[ele for ele in mylist if ele != "#"]

    # 마침표(.)가 처음이나 끝에 위치한다면 제거
    flag = True
    while flag:
        if mylist[0] == ".": # 처음에 오는 값 확인
            del mylist[0]
        elif mylist[-1] == ".": # 마지막에 오는 값 확인
            del mylist[-1]
        # 처음이나 끝에 "."이 없을 때까지 반복
        else:
            flag=False
    
    # 빈 문자열이라면, new_id에 "a"를 대입
    if len(mylist) == 0 : mylist.append("a")

    # 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
    elif len(mylist) >= 16 : 
        del mylist[16:]
        # 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거
        if mylist[-1]==".":
            flag = True
            while flag:
                if mylist[-1] == ".": # 마지막에 오는 값 확인
                    del mylist[-1]
                # 처음이나 끝에 "."이 없을 때까지 반복
                else:
                    flag=False

    # 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙임
    elif len(mylist) <= 2:
        while len(mylist) < 3:
            mylist.append(mylist[-1])
    
    # 리스트를 문자열로 변환
    answer = ''.join(id for id in mylist)
    return answer
print(solution("...!@BaT#*..y.abcdefghijklm"))