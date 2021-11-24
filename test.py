#
# @program: Editor
# @description: oop lab1
# @author: Huang Zihao
# @email: 18302010034@fudan.edu.cn
#
from common.utils.MyIO import MyIO
from handler.executor import Executor

if __name__ == "__main__":
    executor = Executor()
    # commands = MyIO.read_line('手工测试用例/1-命令列表部分/TestCase01.txt')
    # commands = MyIO.read_line('手工测试用例/1-命令列表部分/TestCase02.txt')
    # commands = MyIO.read_line('手工测试用例/2-拼写检查部分/TestCase01/TestCase01.txt')
    # commands = MyIO.read_line('手工测试用例/2-拼写检查部分/TestCase02/TestCase02.txt')
    commands = MyIO.read_line('手工测试用例/3-Bonus/TestCase01/TestCase01.txt')
    for command in commands:
        executor.execute(command)
