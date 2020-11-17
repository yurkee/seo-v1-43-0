import openpyxl

def readexcel():
    #打开文件
    rdexcel = openpyxl.load_workbook('/Users/yurkee/Desktop/seo-v1-43-0/sitemap.xlsx')

    # #通过名称打开表单
    mySheet = rdexcel.active
    # # #直接获取某行某列单元格数据
    myCellValues = mySheet.cell(row=59, column=3).hyperlink.target

    #获取单元格超链接

    print(myCellValues)

readexcel()
