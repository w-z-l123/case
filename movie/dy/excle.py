import xlrd

class duqu(object):

    def __init__(self,name):
        self.name = name

    def get_data(self):
        x = xlrd.open_workbook(self.name)
        sheet = x.sheet_by_index(0)
        hang = sheet.nrows
        b = []
        for i in range(1,hang):
            b.append(sheet.row_values(i))
        return b
if __name__ == '__main__':
    pass


