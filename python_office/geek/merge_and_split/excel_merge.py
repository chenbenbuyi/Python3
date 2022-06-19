import xlrd
'''
支持 Excel 读取的扩展库叫做 xlrd 库，支持 Excel 写入的扩展库叫做 xlwt 库
安装命令：
    pip3 install xlrd 
    pip3 install xlwt
'''


'''
xlrd.biffh.XLRDError: Excel xlsx file; not supported
产生问题的根源是，xlrd这个软件包最新的版本不支持xlsx格式导致的，一般软件更新兼容性会更好，但是这个偏偏是个例，它的兼容性发生了倒退，所以我们使用更早期的版本来实现，excel文件的读取
pip uninstall xlrd
pip install xlrd=1.2.0 (或者更早版本)

'''

def xl():
    path = "C:\\Users\\admin\\Desktop\\相关文档\\12月迭代功能完成情况统计表.xlsx"
    # path = "C:\\Users\\admin\\Desktop\\python.xlsx"
    data = xlrd.open_workbook(path)
    table = data.sheets()[0]
    value = table.cell_value(rowx=1, colx=1)
    print(value)


xl()