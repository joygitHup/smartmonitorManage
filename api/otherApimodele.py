import ast
import requests
from config import smartmonitorSettingFile


def smart_showdevice_list():
    url=smartmonitorSettingFile.smartmonitor_host+smartmonitorSettingFile.smart_show_url
    data=smartmonitorSettingFile.smart_show_data
    new_token = smart_log_authorizations()
    header_dict=ast.literal_eval(smartmonitorSettingFile.smartmonitor_header)
    header_dict['Authorization']='JWT '+'%s'%(new_token)
    requests_re=requests.post(url=url,data=data,headers=header_dict).json()
    return  requests_re

'''轨迹播放'''
def smart_map_show():
    url=smartmonitorSettingFile.map_show_host+smartmonitorSettingFile.map_show_url
    print(url)
    data=smartmonitorSettingFile.map_show_data
    new_token = smart_log_authorizations()
    header_dict = ast.literal_eval(smartmonitorSettingFile.smartmonitor_header)
    header_dict['Authorization'] = 'JWT ' + '%s' % (new_token)
    requests_re = requests.post(url=url, data=data, headers=header_dict).json()
    return  requests_re

'''上传位置信息'''
def smart_map_findloclist():
    url=smartmonitorSettingFile.map_show_host+smartmonitorSettingFile.map_findloclist_url
    data=smartmonitorSettingFile.map_findloclist_data
    new_token = smart_log_authorizations()
    header_dict = ast.literal_eval(smartmonitorSettingFile.smartmonitor_header)
    header_dict['Authorization'] = 'JWT ' + '%s' % (new_token)
    requests_re = requests.post(url=url, data=data, headers=header_dict).json()
    return requests_re