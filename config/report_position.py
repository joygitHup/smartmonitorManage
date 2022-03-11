'''暂未使用起来'''
class Create_report_path:
    '''文件路径'''
    def create_path_savaFile(self):
        '''将报告文件保存到report文件中'''
        path='C:\\DevelopWorkspace\\smartmonitorManage\\report'
        createfile=open(path,'wb')
        createfile.close()

    def creat_path_logpath(self):
        '''创建日志文件'''
        path='C:\DevelopWorkspace\smartmonitorManage\comme\log'
        write_log_topath=open(path,'wb')
        write_log_topath.close()