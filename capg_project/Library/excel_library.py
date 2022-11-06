import xlrd
from Library.config import Configuration


class Readexcel:
    def read_locators(self, sheetname):
        wb = xlrd.open_workbook(Configuration.locators_path)
        ws = wb.sheet_by_name(sheetname)
        columns = ws.ncols
        rows = ws.get_rows()
        header = next(rows)
        data = {}
        for row in rows:
            data[row[0].value] = (row[1].value, row[2].value)
        return data

    def read_test_data(self, sheetname):
        # path = Configuration.test_data
        wb = xlrd.open_workbook(Configuration.test_data)
        ws = wb.sheet_by_name(sheetname)
        rows = ws.get_rows()
        header = next(rows)
        l_ = []
        for row in rows:
            l_.append((row[0].value, row[1].value, row[2].value))

        return l_


#
# r = Readexcel()
# data = r.read_test_data()
# print(data)
