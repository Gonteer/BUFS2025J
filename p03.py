while True :
    t = float(input('당신의 키(m)는?'))
    w = float(input('당신의 몸무게(kg)는?'))
    bmi = w / t ** 2
    print('당신의 bmi는',bmi,'입니다.')

    print('당신은',end=' ')
    if bmi >= 39 :
        print('고도비만',end=' ')
    elif bmi >= 32 :
        print('중도비만',end=' ')
    elif bmi >= 30 :
        print('경도비만',end=' ')
    elif bmi >= 24 :
        print('과체중',end=' ')
    elif bmi >= 10 :
        print('정상',end=' ')
    else : 
        print('저체중',end=' ')

    print('입니다')

    ans = input('계속하시겠습니까(아니요 n)?')
    if ans == 'n' :
        print('이용해 주셔서 감사합니다!\n')
        break
