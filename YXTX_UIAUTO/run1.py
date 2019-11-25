import unittest
import time
from common.HTMLTestRunner_cn import HTMLTestRunner


def creat_suite(lists):
    test_unit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(lists, pattern='test00*.py', top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            test_unit.addTests(test_case)
    return test_unit


list_case = 'all_Case'
all_test = creat_suite(list_case)

now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime(time.time()))
filename = "report\\" + 'result.html'  # 定义个报告存放路径，支持相对路径
fp = open(filename, 'wb')
runner = HTMLTestRunner(stream=fp, verbosity=3,
                        title='亿起点UI自动化测试报告：',
                        description='用例执行结果',
                        retry=1,
                        save_last_try=True)

if __name__ == '__main__':
    runner.run(all_test)