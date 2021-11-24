#
# @program: Editor
# @description: oop lab1
# @author: Huang Zihao
# @email: 18302010034@fudan.edu.cn
#
from handler.executor import Executor

executor = Executor()


def exe(string):
    executor.execute(string)


if __name__ == '__main__':
    # 1-命令列表部分 TestCase02
    exe('-t "To be or not to be"')
    exe('s')            # To be or not to be
    exe('A ", it is"')
    exe('l 1')          # (1, 'A ", it is"')
    exe('l 5')          # (1, 'A ", it is"')
    exe('a "No. "')
    exe('m 2 ADD')
    exe('u')
    exe('s')            # To be or not to be, it is
    exe('u')
    exe('s')            # To be or not to be
    exe('u')
    exe('s')            # To be or not to be
    exe('r')
    exe('s')            # To be or not to be, it is
    exe('r')
    exe('s')            # No. To be or not to be, it is
    exe('r')
    exe('s')            # No. To be or not to be, it is
    exe('l 2')          # (1, a "No. ") (2, A ", it is")
    exe('l 10')         # (1, a "No. ") (2, A ", it is")
    exe('r')
    exe('s')            # No. To be or not to be, it is
    exe('$ADD')
    exe('s')            # No. No. To be or not to be, it is, it is
    exe('u')
    exe('s')            # No. To be or not to be, it is
    exe('r')
    exe('s')            # No. No. To be or not to be, it is, it is
    exe('l 2')          # (1, $ADD) (2, a "No. ")
