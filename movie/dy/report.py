import unittest,yagmail
from BeautifulReport import BeautifulReport

reportname = '维度电影'

if __name__ == '__main__':

    suite = unittest.defaultTestLoader.discover('./',pattern='movie*.py')
    a = BeautifulReport(suite)
    a.report(filename=reportname,description='执行用例')

    mail = yagmail.SMTP(user='2501212849@qq.com',
                     password='jyhgobpvrriweaid',
                     host='smtp.qq.com')
    mail.send(to='2501212849@qq.com', subject='月考',contents=[reportname])






