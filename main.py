import HTMLTestRunner
import time
import unittest
from api.smart_log_api import smart_log_api_test

from config.send_report_email_ import sendEmai

if __name__=="__main__":
    test_suit = unittest.TestSuite()
    test_suit.addTest(smart_log_api_test('smart_log_authorizations_crent'))
    test_suit.addTest(smart_log_api_test('smart_log_authorizations_error'))
    test_suit.addTest(smart_log_api_test('smart_log_authorizations_user_error'))
    runtest = unittest.TextTestRunner()
    # 创建生成结果文件格式 且写入文件
    now_time = time.strftime('%Y-%m-%d %H_%M_%S')

    filepath = 'C:\\Users\\Administrator\\Desktop\\smartmonitorManage\\report'
    filename = filepath + "\\" + now_time + 'report.html'
    fb = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fb, title='软件测试HTML报告', description='测试报告')
    runner.run(test_suit)
    fb.close()
    # 将结果通过邮件发送到指定人
    send_emai = sendEmai()
    send_emai.Sendemail(newfile=filename)