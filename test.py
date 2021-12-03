#
# @program: Editor
# @description: oop lab1
# @author: Huang Zihao
# @email: 18302010034@fudan.edu.cn
#
import sys, difflib
from common.utils.MyIO import MyIO
from handler.executor import Executor


def auto_test(input_file, output_file, std_answer):
    executor = Executor()
    saved_stdout = sys.stdout
    commands = MyIO.read_line(input_file)
    with open(output_file, 'w') as file:
        sys.stdout = file
        for command in commands:
            executor.execute(command)

    sys.stdout = saved_stdout
    want_results = open(std_answer).readlines()
    actual_results = open(output_file).readlines()
    diff = difflib.ndiff(want_results, actual_results)
    # print("标准答案与实际输出为")
    # print("注：+ -号标注的行为不同行，？为不同的地方")    # 如果需要查看标准答案和实际输出的差别，请取消这个函数内的三行注释
    is_pass = True
    for i in diff:
        # print(i)
        if '+' in i or '-' in 'i':
            is_pass = False
    if is_pass:
        print(input_file + " 测试用例通过！")
    else:
        print(input_file + " 测试用例不通过！")


if __name__ == "__main__":
    # 这5个auto_test分别自动测试5个给出的测试用例，取消和加上对应的注释语句即可
    auto_test('手工测试用例/1-命令列表部分/TestCase01.txt', '手工测试用例/1-命令列表部分/TestCase01Output.txt',
              '手工测试用例/1-命令列表部分/TestCase01Want.txt')
    # auto_test('手工测试用例/1-命令列表部分/TestCase02.txt', '手工测试用例/1-命令列表部分/TestCase01Want.txt',
    #           "手工测试用例/1-命令列表部分/TestCase02Want.txt")
    # auto_test('手工测试用例/2-拼写检查部分/TestCase01/TestCase01.txt', "手工测试用例/2-拼写检查部分/TestCase01/TestCase01Output.txt",
    #           "手工测试用例/2-拼写检查部分/TestCase01/TestCase01Want.txt")
    # auto_test('手工测试用例/2-拼写检查部分/TestCase02/TestCase02.txt', "手工测试用例/2-拼写检查部分/TestCase02/TestCase02Output.txt",
    #           "手工测试用例/2-拼写检查部分/TestCase02/TestCase02Want.txt")
    # auto_test('手工测试用例/3-Bonus/TestCase01/TestCase01.txt', "手工测试用例/3-Bonus/TestCase01/TestCase01Output.txt",
    #           "手工测试用例/3-Bonus/TestCase01/TestCase01Want.txt")
