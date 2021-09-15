import xlwt

class xlwttt(object):

    def __init__(self):
        pass

    def write_date(self):
        a = xlwt.Workbook(encoding='utf-8')
        b = a.add_sheet('s1')
        b.write(0,0,'你好')
        a.save()


if __name__ == '__main__':
    pass