# encoding utf-8
from common.base import Base
from common.readexcel import ExcelUtil


def datas():
    filepath = "../all_Case/testdata.xlsx"
    sheetName = "Sheet1"
    data = ExcelUtil(filepath, sheetName)
    testdata=data.dict_data()
    return testdata

