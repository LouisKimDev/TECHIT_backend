from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def calculator(request):
    # return HttpResponse('계산기 기능 구현 시작합니다')
    print(f'request= {request}')

    # 1. 데이터 확인
    num1 = request.GET.get('num1') # 값 1
    num2 = request.GET.get('num2') # 값 2
    operators = request.GET.get('operators') # 계산할 연산자
    print(num1)
    
    # 2. 계산
    if operators == '+':
        result = int(num1) + int(num2)
    elif operators == '-':
        result = int(num1) - int(num2)
    elif operators == '*':
        result = int(num1) * int(num2)
    elif operators == '/':
        result = int(num1) / int(num2)
    else:
        result = 0


    # 3. 응답
    # request를 받아서 calculator을 rendering 함
    return render(request, 'calculator.html', {'result': result})
    