import os
from time import sleep
from random import choice

def drawTitle():
    print('ㅤㅤㅤㅤㅤㅤ■ㅤㅤㅤ■ㅤㅤ■■■ㅤㅤ■ㅤㅤㅤ■ㅤ■■■■■ㅤ■ㅤㅤㅤ■')
    print('ㅤㅤㅤㅤㅤㅤ■■ㅤ■■ㅤ■ㅤㅤㅤ■ㅤ■■ㅤㅤ■ㅤㅤㅤ■ㅤㅤㅤㅤ■ㅤ■ㅤ')
    print('ㅤㅤㅤㅤㅤㅤ■ㅤ■ㅤ■ㅤ■ㅤㅤㅤ■ㅤ■ㅤ■ㅤ■ㅤㅤㅤ■ㅤㅤㅤㅤㅤ■ㅤㅤ')
    print('ㅤㅤㅤㅤㅤㅤ■ㅤ■ㅤ■ㅤ■ㅤㅤㅤ■ㅤ■ㅤㅤ■■ㅤㅤㅤ■ㅤㅤㅤㅤㅤ■ㅤㅤ')
    print('ㅤㅤㅤㅤㅤㅤ■ㅤ■ㅤ■ㅤㅤ■■■ㅤㅤ■ㅤㅤㅤ■ㅤㅤㅤ■ㅤㅤㅤㅤㅤ■ㅤㅤ')
    print()
    print('ㅤㅤㅤㅤㅤㅤㅤㅤㅤ■ㅤㅤㅤ■ㅤㅤㅤ■ㅤㅤㅤ■ㅤㅤㅤㅤㅤ■ㅤㅤㅤㅤ')
    print('ㅤㅤㅤㅤㅤㅤㅤㅤㅤ■ㅤㅤㅤ■ㅤㅤ■ㅤ■ㅤㅤ■ㅤㅤㅤㅤㅤ■ㅤㅤㅤㅤ')
    print('ㅤㅤㅤㅤㅤㅤㅤㅤㅤ■■■■■ㅤ■■■■■ㅤ■ㅤㅤㅤㅤㅤ■ㅤㅤㅤㅤ')
    print('ㅤㅤㅤㅤㅤㅤㅤㅤㅤ■ㅤㅤㅤ■ㅤ■ㅤㅤㅤ■ㅤ■ㅤㅤㅤㅤㅤ■ㅤㅤㅤㅤ')
    print('ㅤㅤㅤㅤㅤㅤㅤㅤㅤ■ㅤㅤㅤ■ㅤ■ㅤㅤㅤ■ㅤ■■■■■ㅤ■■■■■')
    print()
    print('■■■■ㅤㅤ■■■■■ㅤ■ㅤㅤㅤㅤㅤ■■■■■ㅤ■ㅤㅤㅤ■ㅤ■ㅤㅤㅤ■ㅤㅤㅤ■ㅤㅤ')
    print('■ㅤㅤㅤ■ㅤㅤㅤ■ㅤㅤㅤ■ㅤㅤㅤㅤㅤ■ㅤㅤㅤㅤㅤ■■ㅤ■■ㅤ■■ㅤ■■ㅤㅤ■ㅤ■ㅤ')
    print('■ㅤㅤㅤ■ㅤㅤㅤ■ㅤㅤㅤ■ㅤㅤㅤㅤㅤ■■■■ㅤㅤ■ㅤ■ㅤ■ㅤ■ㅤ■ㅤ■ㅤ■■■■■')
    print('■ㅤㅤㅤ■ㅤㅤㅤ■ㅤㅤㅤ■ㅤㅤㅤㅤㅤ■ㅤㅤㅤㅤㅤ■ㅤ■ㅤ■ㅤ■ㅤ■ㅤ■ㅤ■ㅤㅤㅤ■')
    print('■■■■ㅤㅤ■■■■■ㅤ■■■■■ㅤ■■■■■ㅤ■ㅤ■ㅤ■ㅤ■ㅤ■ㅤ■ㅤ■ㅤㅤㅤ■')


def clearConsole(time: int):
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    
    sleep(time)
    os.system(command)

def selectCnt():
    cnt = input('시행할 횟수를 적어주세요 : ')
    while not cnt.isnumeric():
        print('입력에 오류가 일어났습니다. 다시 입력해주세요.')
        clearConsole(3)
        cnt = input('시행할 횟수를 적어주세요 : ')

    return int(cnt)

def selectRound():
    rnd = input('올림할 소수점 자릿수를 적어주세요(0 ~ 15) : ')
    while (not rnd.isnumeric()) or (int(rnd) > 15):
        print('입력에 오류가 일어났습니다. 다시 입력해주세요.')
        clearConsole(3)
        rnd = input('올림할 소수점 자릿수를 적어주세요(0 ~ 15) : ')

    return int(rnd)


drawTitle()
sleep(3)

operationCnt = selectCnt()
roundingPoint = selectRound()
successCnt = 0
rate = 0

for tryCnt in range(operationCnt):
    option = [1, 2, 3]
    initSelection = choice(option)
    car = choice(option)

    if initSelection == car:
        option.remove(car)
        anotherGoat = choice(option)
        option.remove(anotherGoat)
        finalSelection = choice(option)
        result = '실패 '
    
    else:
        option.remove(initSelection)
        option.remove(car)
        anotherGoat = choice(option)
        finalSelection = car
        result = '성공!'
        successCnt += 1

    rate = successCnt / (tryCnt+1) * 100

    print('{0}회    |    정답 : {1}    첫 선택 : {2}    오답 확인 : {3}    다른 선택 : {4}    결과 : {5} ... {6}%'.
    format(tryCnt+1, car, initSelection, anotherGoat, finalSelection, result, round(rate, roundingPoint)))

os.system('pause')