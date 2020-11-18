import openpyxl

def readexcel():
    #打开文件
    rdexcel = openpyxl.load_workbook('/Users/yurkee/Desktop/seo-v1-43-0/sitemap.xlsx')

    # #通过名称打开表单
    mySheet = rdexcel.active
    #直接获取某行某列单元格数据
    # myCellValues = mySheet.cell(row=59, column=3).hyperlink.target

    for row in mySheet.iter_rows():
        for cell in row:
            if cell.value != None:
                myLink = cell.hyperlink.target[22:]
        print(myLink)

    # mycell = mySheet.cell(row=1, column=1).hyperlink.target
    # print(mycell)

    #获取单元格超链接

    # print(myCellValues)

readexcel()
