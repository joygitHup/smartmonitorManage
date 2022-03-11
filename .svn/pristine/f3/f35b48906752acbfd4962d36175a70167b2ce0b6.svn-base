import HTMLTestRunner
import time
import unittest
import  requests
from config import smartmonitorSettingFile

class smart_log_api_test(unittest.TestCase):
    '''初始化loginApi的请求路径'''
    def setUp(self) :
        self.base_url=smartmonitorSettingFile.smartmonitor_host+smartmonitorSettingFile.smart_log_api_url
    def smart_log_authorizations_crent(self):
      '''用户名和密码都正确'''
      url=self.base_url
      data=smartmonitorSettingFile.smart_log_api_date
      requests_result=requests.post(url=url,data=data,headers=eval(smartmonitorSettingFile.smartmonitor_header)).json()
      # self.assertEqual(requests_result['username'],'ybx')
      if requests_result['username']=='ybx':
        print('ybx登录成功！')
      else:
        print('请检查用户名和密码')
      return  requests_result['token']
    def smart_log_authorizations_error(self):
      '''另一个用户名和密码'''
      url=self.base_url
      data=smartmonitorSettingFile.smart_log_api_date_error
      requests_result=requests.post(url=url,data=data,headers=eval(smartmonitorSettingFile.smartmonitor_header)).json()
      # self.assertEqual(requests_result['username'],'ybx')
      if requests_result['password']=='12345678':
        print('ybx登录成功！')
      else:
        print('请检查用户名和密码')
      return  requests_result['token']
    def smart_log_authorizations_user_error(self):
      """正确的用户名错误的密码"""
      url=self.base_url
      data=smartmonitorSettingFile.smart_log_api_date_error1
      requests_result=requests.post(url=url,data=data,headers=eval(smartmonitorSettingFile.smartmonitor_header)).json()
      # self.assertEqual(requests_result['username'],'ybx')
      '''断言是否登录成功'''
      if requests_result['username']=='lxf':
        print('{}登录成功！'.format(requests_result['username'],'lxf'))
        print('%s登录成功！'%requests_result['username'],'lxf')
      else:
        print('请检查用户名和密码')
      return  requests_result['token']

    def tearDown(self):
        pass
if __name__=="__main__":
    # 继承所有的testcase  有两种方式 1.一个一个往里面装  2.通过discover批量装入case
    test_suit=unittest.TestSuite()
    test_suit.addTest(smart_log_api_test('smart_log_authorizations_crent'))
    test_suit.addTest(smart_log_api_test('smart_log_authorizations_error'))
    test_suit.addTest(smart_log_api_test('smart_log_authorizations_user_error'))
    runtest=unittest.TextTestRunner()
    # 创建生成结果文件格式 且写入文件
    now_time=time.strftime('%Y-%m-%d %H_%M_%S')
    filepath='C:\\DevelopWorkspace\\smartmonitorManage\\report'
    filename=filepath+"\\"+now_time+'_report.html'
    fb=open(filename,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fb,title='软件测试HTML报告',description='测试报告')
    runner.run(test_suit)
    fb.close()
    # 将结果通过邮件发送到指定人
    # send_emai = sendEmai()
    # send_emai.Sendemail(newfile=filename)
    # requests_re=smart_map_findloclist()
    # print(requests_re)
    # requests_re=smart_log_authorizations()
    # print(requests_re)
    # requests_re=smart_zegogdp_connection()
    # print(requests_re)
    # requests_re=smart_showdevice_list()
    # print(requests_re)
