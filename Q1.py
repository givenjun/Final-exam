# Q.1 10점
#
# 문자열 my_string과 target이 매개변수로 주어질 때,
# target이 문자열 my_string의 부분 문자열이라면 1을,
# 아니라면 0을 return 하는 solution 함수를 작성하시오.
#
# 제한사항
# 1 ≤ my_string 의 길이 ≤ 100
# my_string 은 영소문자로만 이루어져 있습니다.
# 1 ≤ target 의 길이 ≤ 100
# target 은 영소문자로만 이루어져 있습니다.

def solution(my_string, target):
    if(my_string.find(target) == -1): #my_string.find(target)값이 -1이면 실행 (찾는 문자열이 없으면 -1 반환)
        answer = 0 #즉, target이 my_string의 부분 문자열이 아니므로 answer = 0 저장
    else: #my_string.find(target)값이 -1이 아니면 실행 (찾는 문자열이 처음 나온 인덱스 위치 반환)
        answer = 1 #즉, target이 my_string의 부분 문자열이므로 answer = 1 저장
    return answer


