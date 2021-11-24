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
    # 1-命令列表部分 TestCase01
    exe('A "world"')
    exe('a "Hello "')
    exe('s')    # Hello world
    exe('D 2')
    exe('d 7')
    exe('D 5')
    exe('A "Hi world"')
    exe('s')    # Hi world
    exe('d 30')
    exe('s')    #
