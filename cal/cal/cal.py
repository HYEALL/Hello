#4강에서 만들었던 계산기를 기능별로 함수로 만들고 계산결과는 txt파일에 저장되도록 만드는거입니다
get_num1 = 0
get_num2 = 0
get_ = 0
er = 0
get_math = 0
def start():
    global get_
    print("종료하려면 e, 재시작 하시려면 c를 입력해주세요.")

    get_ = input("계산식을 입력해주세요>>>")


def operator():
    global get_math,er
    global get_
    global get_num1, get_num2
    if '+' in get_:
        get_num1, get_num2 = get_.split("+")
        get_math = '+'

    elif '-' in get_:
        get_num1, get_num2 = get_.split('-')
        get_math = '-'

    elif '*' in get_:
        get_num1, get_num2 = get_.split("*")
        get_math = '*'

    elif '/' in get_:
        get_num1, get_num2 = get_.split("/")
        get_math = '/'

    else:
        print("잘못된 입력입니다. 올바른 연산자를 입력해주세요.")
        er = 1
        return 0

    get_num1 = get_num1.strip()
    get_num2 = get_num2.strip()

    if not get_num1.isdigit() or not get_num2.isdigit():
        print("잘못된 입력입니다. 숫자를 입력해주세요.")
        er = 1

def cal():
    if get_math == '+':
        file = open("result.txt",'w')
        file.write(f"결과값은 {int(get_num1) + int(get_num2)}입니다.")
        file.close()

    elif get_math == '-':
        file = open("result.txt", 'w')
        file.write(f"결과값은 {int(get_num1) - int(get_num2)}입니다.")
        file.close()

    elif get_math == '*':
        file = open("result.txt", 'w')
        file.write(f"결과값은 {int(get_num1) * int(get_num2)}입니다.")
        file.close()

    elif get_math == '/':
        file = open("result.txt", 'w')
        file.write(f"결과값은 {int(get_num1) / int(get_num2)}입니다.")
        file.close()

while True:
    er = 0
    start()
    if get_ == 'c':
        continue
    elif get_ == 'e':
         break
    operator()
    if er == 1:
        continue
    cal()

