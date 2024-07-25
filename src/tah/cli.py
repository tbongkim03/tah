import argparse
from tah.db.utils import count, top
def hello_msg():
    return "hello"

def cmd11():
    parser = argparse.ArgumentParser(
            prog="ProgramName",
            description='What the program does',
            epilog='Text at the bottom of help')

    parser.add_argument('-s', '--scount')
    parser.add_argument('-t', '--top') # option that takes a value
    parser.add_argument('-d', '--dt') # on/off flag 값이 있으면 true 출력

    args = parser.parse_args()

    if args.scount:
        command = args.count
        count = count(command)
        print(f'cmd : {command}를 사용한 횟수는 {count}회 입니다.')
    elif args.top:
        if args.dt:
            num, date = int(args.top), args.dt
            top_n = top(num, date)
            print(top_n)
        else:
            parser.error('이 -t <Num>option는 -d <YYYY-MM-DD>와 함께 사용하세요')
            pass
    else:
        parser.print_help()
