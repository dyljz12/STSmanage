import os
import pickle
from lib import *


def teachercontrol():
    print("This is teacher management view.")
    teacherobj = Teacher.Teacher()
    name = input("请输入您的名字：")
    fddir = os.path.dirname(os.path.dirname(__file__))
    with open('%s\dumpfile\\teacher\%s' % (fddir, name), 'rb') as fd:
        teacherobj = pickle.load(fd)


    teachermanageoptdic = { '1': teacherobj.checkgroupinfo, '2': teacherobj.changescore, '3': exit}
    flag = True
    while flag:
        teachermanopt = input("你要干什么？\n1：查看班级信息\n2：登记学生成绩\n3:退出\n")
        if teachermanopt in teachermanageoptdic.keys():
            teacherobj = teachermanageoptdic[teachermanopt]()
    return
