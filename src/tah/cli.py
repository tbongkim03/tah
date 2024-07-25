import argparse
from tah.db.utils import count, top
def hello_msg():
    return "hello"

def cmd11():
    msg = hello_msg()
    print(msg)
   
    parser = argparse.ArgumentParser(
            prog="ProgramName",
            description='What the program does',
            epilog='Text at the bottom of help')

    parser.add_argument('-s', '--scount')
    #parser.add_argument('filename') # positional argument
    parser.add_argument('-t', '--top') # option that takes a value
    parser.add_argument('-d', '--dt') # on/off flag 값이 있으면 true 출력

    args = parser.parse_args()
    print(args.scount, args.top, args.dt)

    if args.scount:
        cmd_cnt = count(args.scount)
        print(cmd_cnt)
        #print(f"-s -> {args.scount}")
        # TODO 명령어 카운트

    elif args.top:
        print(f"-t -> {args.top}")
        if args.dt:
            print(f"-d -> {args.dt}")
            # TODO 특정 날짜의 명령어 TOP N
            top_n = top(args.top, args.dt)
            print(top_n)
        else:
            #TODO 에러나 안내메시지
            parser.error('이 -t <Num>option는 -d <YYYY-MM-DD>와 함께 사용하세요')
            pass
    else:
        parser.print_help()
