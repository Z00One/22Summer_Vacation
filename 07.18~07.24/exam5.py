myList       = "!! hello world, it is awesome day."
exoCharCount = 0    # 특수문자
wordCount    = 0    # 단어 수
blankCount   = 0    # 공백 수

for index in range(len(myList)):
    # 다음 값
    nextChar = "" if index == len(myList) - 1 else myList[index + 1]
    # 특수 문자
    if myList[index] == "!" or myList[index] == "," or myList[index] == ".":
        exoCharCount += 1
    # 단어
    if myList[index].isalpha() and not(nextChar.isalpha()):
        wordCount += 1
    # 공백
    if myList[index] == " ":
        blankCount += 1

print("특수문자 수 :", exoCharCount)
print("단어 수 :", wordCount)
print("특수문자 제외 글자수 :", len(myList) - exoCharCount - blankCount) 