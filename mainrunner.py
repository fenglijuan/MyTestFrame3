from common.Excel import *
from inter.Http import *
import inspect
'''这是自动化框架的主代码运行入口
powered by fenglj   at 2019/12/19'''
# print('该功能暂未实现')
# from inter import interrnner
def runcase(line,f):
    if len(line[0])>0 or len(line[1])>0:
        return
    #反射获取关键字函数
    func = getattr(f, line[3])
    #获取参数列表
    args = inspect.getfullargspec(func).__str__()
    #print(args)
    #print(func.__doc__)
    args = args[args.find('args=') + 5:args.rfind(', varargs=')]
    #print(args)
    args = eval(args)
    args.remove('self')
    #print(args)
    #print(len(args))
    if len(args)==0:
        func()
        return
    if len(args)==1:
        func(line[4])
        return
    if len(args)==2:
        func(line[4],line[5])
        return
    if len(args)==3:
        func(line[4],line[5],line[6])
        return
    print('Error:目前只支持3个关键字的参数')
#     #使用条件语句，判断字符串，然后调用指定方法
#     if line[3]=='post':
#         http.post(line[4],line[5],line[6])
#         return
#     if line[3]=='assertequals':
#         http.assertequals(line[4],line[5])
#         return

reader = Reader()
reader.open_excel('./lib/HTTP接口用例.xls')
sheetname = reader.get_sheets()
writer = Writer()
writer.copy_open('./lib/HTTP接口用例.xls', './lib/result-HTTP接口用例.xls')
#sheetname = writer.get_sheets()
http=HTTP(writer)
#writer.write(1, 1, 'William')

for sheet in sheetname:
    # 设置当前读取的sheet页面
    reader.set_sheet(sheet)
    #保存读写在同一个sheet页面
    writer.set_sheet(sheet)
    for i in range(reader.rows):
        #print(reader.readline())
        writer.row=i
        line=reader.readline()
        runcase(line,http)
writer.save_close()