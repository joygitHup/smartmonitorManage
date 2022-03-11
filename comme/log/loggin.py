import logging

from logging import handlers

class mylogger():
    def __init__(self,file_name,level='info',backCount=5,when='D'):
        logger = logging.getLogger()  # 实例化一个logger对象
        logger.setLevel(self.get_level(level))  # 设置日志级别
        cl = logging.StreamHandler()  # 负责往控制台输出
        bl = handlers.TimedRotatingFileHandler(filename=file_name, when=when, interval=1, backupCount=backCount, encoding='utf-8')
        fmt = logging.Formatter('%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')
        # 输出格式
        cl.setFormatter(fmt)  # 设置控制台输出的日志格式
        bl.setFormatter(fmt)  # 设置文件里面写入的日志格式
        logger.addHandler(cl)  # 把已经做好格式处理的人放到办公室里
        logger.addHandler(bl)
        self.logger=logger
    def get_level(self,str):
        level={
            'debug':logging.DEBUG,
            'info':logging.INFO,
            'warn':logging.WARNING,
            'error':logging.ERROR
        }
        str==str.lower()
        return level.get(str)


#实例化，用的时候就不用实例化了；不加.logger调用的时候需要atp_log.logger.waring;现在只需要atp_log.waring
