from pathlib import Path, PurePath
import datetime
from docx import Document
import xlrd

today = datetime.date.today().strftime('%Y-%m-%d')

# 替换内容
replace_content = {
    '<姓名>': 'no_name',
    '<性别>': 'm_f',
    '<今天日期>': today
}

# 邀请函生成
def generat_invitation():

    doc = Document('word/邀请函模版.docx')

    # 取出每一段
    for para in doc.paragraphs:
        for key, value in replace_content.items():
            if key in para.text:
                # 逐个关键字进行替换
                para.text = para.text.replace(key, value)

    # 这种函数定义路径的方式会把下层路径替换为后面的名称 要求目录必须先存在
    file_name = PurePath('word/邀请函/随便写').with_name(replace_content['<姓名>']).with_suffix('.docx')

    doc.save(file_name)


# 从 excel红获取人员信息
def get_customer(customer_file: Path):

    # 从第一个sheet中取出客户信息
    data = xlrd.open_workbook(customer_file)
    table = data.sheets()[0]

    # 取得客户数量
    customer_number = table.nrows

    for line in range(1, customer_number):
        content = table.row_values(rowx=line, start_colx=0, end_colx=None)
        replace_content['<姓名>'] = content[0]
        replace_content['<性别>'] = content[1]
        print(replace_content)
        generat_invitation()


if __name__ == '__main__':
    get_customer('word/客户信息.xls')
