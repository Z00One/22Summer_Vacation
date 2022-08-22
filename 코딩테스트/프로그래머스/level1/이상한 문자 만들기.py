def solution(s):
    answer = ''
    count = 0
    for index in range(len(s)):
        if s[index] == " ":
            count = -1
        if count % 2 == 0:
            answer += s[index].upper()
        else:
            answer += s[index].lower()
        count +=1
    return answer

print(solution("           sdkas skdsd sds sa             d"))