from django.shortcuts import render
from django.http import HttpResponse
import random

def lotto(request):
    # return HttpResponse('로또 번호 추출기 기능 시작')
    
    # 1. 데이터 확인
    print(f'request= {request}')

    # if request.GET.get('num') == None:
    #     num = 1
    # else:
    #     num = request.GET.get('num')

    num = request.GET.get('num', 1)

    result = [[0 for i in range(6)] for i in range(int(num))]

    for i in range(int(num)):
        for j in range(6):
            temp1 = random.randint(1,45)
            while temp1 in result[i]:
                temp1 = random.randint(1,45)           
            result[i][j]= temp1
    
    
    # 3. 응답
    # request를 받아서 lotto을 rendering 함
    return render(request, 'lotto.html', {'result': result, 'num':num})
    