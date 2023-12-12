# Q.2 10점
#
# 모스부호 해독 프로그램 만들기
# 문자열 letter 가 매개변수로 주어질 때,
# letter 영어 소문자로 바꾼 문자열을 return 하는
# solution 함수를 완성하시오.
#
# 제한사항
# 1 ≤ letter 의 길이 ≤ 1,000
# letter 의 모스부호는 공백으로 나누어져 있습니다.
# letter 에 공백은 연속으로 두 개 이상 존재하지 않습니다.
#
# letter = 여러분의 좌우명 또는 인상 깊었던 말을 쓰시오.

def solution(letter):
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}
    #모스부호 <-> 알파벳 관계를 나타내는 morse 딕셔너리 설정 

    wordlist = letter.split(' ')
    #letter 문자열을 공백을 기준으로 나눠서 리스트로 반환

    answer = '' #answer값 초기화

    for word in wordlist:
    #wordlist 리스트의 첫 번째 요소부터 마지막 요소까지 차례로 word에 대입되며 반복수행
        if word in morse:
        #morse 딕셔너리에 해당 모스 부호(key)가 존재하는 경우에만 실행
            answer += morse[word]
            #해당 모스 부호(key)에 대응하는 알파벳(value)를 answer에 더하고 저장 
    return answer



