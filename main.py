#
# @program: Editor
# @description: oop lab1
# @author: Huang Zihao
# @email: 18302010034@fudan.edu.cn
#
from handler.executor import Executor

if __name__ == '__main__':
    executor = Executor()
    while True:
        executor.execute(input())
