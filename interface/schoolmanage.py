from lib import *
import pickle
import os


def schoolcontrol():
    print("This is school management view.")
    schoolobj = School.School()    #???????????1.语法(因为要调用School，不再一个文件里)。2.为什么不用.lib

    def chooseschool():
        namein = input("请输入学校名字：")
        fddir = os.path.dirname(os.path.dirname(__file__))
        with open('%s/dumpfile/school/%s' % (fddir, namein), 'rb') as fd:
            schoolobj = pickle.load(fd)
        schoolobj.getteacher()
        schoolobj.getcourse()
        schoolobj.getgroup()
        schoolobj.getstudent()
        return schoolobj

    schoolmanageoptdic0 = {'1': schoolobj.setschool, '2': chooseschool, '3': exit}
    flag = True
    while flag:
        schoolmanopt = input("你要干什么？\n1：建校\n2：选择学校\n3:退出\n")

        if schoolmanopt in schoolmanageoptdic0.keys():
            schoolobj = schoolmanageoptdic0[schoolmanopt]()
        if schoolmanopt=='2':
            break


    schoolmanageoptdic = {'1': schoolobj.addteacher,
                          '2': schoolobj.addcourse, '3': schoolobj.addgroup, '4': exit}
    flag = True
    while flag:
        schoolmanopt = input("你要干什么？\n1：招聘老师\n2：开设课程\n3：开设班级\n4:退出\n")
        if schoolmanopt in schoolmanageoptdic.keys():
            schoolobj = schoolmanageoptdic[schoolmanopt]()
    return
