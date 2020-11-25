# coding=utf-8
import openpyxl

def readexcel():
    #打开文件
    rdexcel = openpyxl.load_workbook('D:\work\seo-v1-43-0\sitemap.xlsx')

    #通过名称打开表单，打开默认表格
    mySheet = rdexcel.active

    #读取指定的表格
    # mySheet = rdexcel.get_sheet_by_name('Sheet2')

    #直接获取某行某列单元格数据
    # myCellValues = mySheet.cell(row=59, column=3).hyperlink.target
    # myCellLink = mySheet.cell(row=1, column=1).value
    # print(myCellLink)


    #获取一个单元格中的文字信息和超链接，组成字典存储
    # myTablename = mySheet.cell(row=1, column=1).value
    # myTablelink = mySheet.cell(row=1, column=1).hyperlink.target[22:]
    # myList = {myTablename: myTablelink}
    # print(myList)

    # 用列表的方式存储读取的link
    # myList = []
    # for row in mySheet.iter_rows():
    #     for cell in row:
    #         if cell.value != None:
    #             myLink = cell.hyperlink.target[22:]
    #             myList.append(myLink)
    # print(myList)

    #用字典的方式存储，从表格中读取的单元格值和超链接
    myTableDicValue = {}
    for row in mySheet.iter_rows():
        for cell in row:
            if cell.value != None:
                myTableValue = cell.value
                myTableLink = cell.hyperlink.target[22:]
                Dict = {myTableValue: myTableLink}
                myTableDicValue.update(Dict)
    # print(myTableDicValue)
    return myTableDicValue

