# Q.3 10점
#
# 행성의 나이를 알파벳으로 표현할 때,
# a는 0, b는 1, ..., j는 9
# 예를 들어 cd는 23살, fb는 51살입니다.
# age가 매개변수로 주어질 때
# PROGEAMMER-857식 나이를 return 하도록
# solution 함수를 완성하시오.
#
# 제한사항
# age는 자연수입니다.
# age ≤ 1,000
# PROGRAMMERS-857 행성은 알파벳 소문자만 사용합니다.

def solution(age):
    alphabet = 'abcdefghij'  #행성의 나이 표현을 위해 문자열 생성
    answer = '' #answer값을 초기화

    while age != 0: #age값이 0이 아니면 반복수행 
        index = (age) % 10 #문자열 alphabet의 index를 age를 10으로 나눈 나머지값으로 설정
        answer = alphabet[index] + answer #answer값에 alphabet[index]와 그 전 answer를 더한 값으로 설정
        age = (age) // 10 #age값에 그 전 age를 10으로 나눈 몫값으로 설정 -> age가 일의 자리만 남으면
                          #몫이 없으므로 age는 0이 되고 while문 탈출

    return answer




