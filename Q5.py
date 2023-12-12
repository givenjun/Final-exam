# Q.5 10점
#
# 0 또는 양의 정수가 주어졌을 때,
# 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
#
# 예를 들어, 주어진 정수가 [6, 10, 2]라면
# [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
# 이중 가장 큰 수는 6210입니다.
#
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어
# return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
#
# numbers = [8, 30, 17, 2, 23]

def solution(numbers):
    answer = ''
    #answer값 초기화
    numbers = list(map(str, numbers))
    #주어진 numbers의 각 요소를 문자열로 변환시킨 리스트로 numbers에 저장
    #list(map(str, numbers)) -> map(str, numbers)를 입력받아 리스트로 만들어 리턴
    #map(str, numbers) -> 함수 str과 numbers를 입력받아 str(numbers)의 결과 리턴 
    #str() -> 문자열 형태로 객체를 변환하여 리턴하는 함수

    for i in range(0, len(numbers)):
            numbers[i] = numbers[i]*3
    #numbers[i] * 3 을 통해 numbers 리스트의 전체 요소에 문자열 곱셈
    #ex) ["2", "23", "20"] -> ["222", "232323", "202020"]
    numbers.sort()
    numbers.reverse()
    #가장 큰 수로 재배치되도록 numbers를 sort() => 내림차순 정렬하고 
    #reverse() => 거꾸로 정렬(오름차순)
   
    for i in range(0, len(numbers)):
            if len(numbers[i]) == 3:
                numbers[i] = numbers[i][:1]
            elif len(numbers[i]) == 6:
                numbers[i] = numbers[i][:2]
            elif len(numbers[i]) == 9:
                numbers[i] = numbers[i][:3]
            elif len(numbers[i]) == 12:
                numbers[i] = "1000"
    #numbers의 각 요소가 한 자리수, 두 자리수, 세 자리수일 수 있는데
    #문자열 곱셈 후에는 리스트 각 요소의 길이가 3배로 증가
    #한 자리수인 요소 길이 = 3 / 두 자리수인 요소 길이 = 6 / 세 자리수인 요소 길이 = 9 / "1000" 길이 = 12
    #요소 길이가 3이면 numbers[i][:1] 슬라이싱, 6이면 numbers[i][:2] 슬라이싱, 9면 numbers[i][:3] 슬라이싱, 12면 "1000"
    
    #-------------------문자열 * 3 결과를 정렬하는 이유--------------------
    #numbers = ["2", "23", "20"]을 기준으로 정렬하면 ["23", "20", "2"] 
    #numbers*3 = ["222", "232323", "202020"]을 기준으로 정렬하면 ["232323", "222", "202020"]
    #문자열을 정렬할 때, 문자열 인덱싱을 통해 요소 마다의 크기를 비교
    #numbers -> 23202 / numbers*3 -> 23220

    answer = str(int(''.join(numbers)))
    #numbers의 문자열 요소를 삽입해 하나의 문자열로 만들고 정수형으로 변환 후 
    #다시 문자열로 변환하여 answer에 저장
    #str(int(''.join(numbers)) -> (int(''.join(numbers))를 입력받아 문자열로 만들어 리턴
    #int(''.join(numbers)) -> (''.join(numbers))를 입력받아 정수형으로 만들어 리턴
    # -> 맨 처음 입력받은 numbers의 요소에서 0만 있을 때, 000...00...0이 0으로 바꾸기 위해서
    #''.join(numbers) -> 공백없이 numbers의 문자열 요소들을 하나의 문자열로 삽입
    return answer




