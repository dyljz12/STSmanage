from lib import *
import pickle
import os


def studentcontrol():
    print("This is student management view.")
    studentobj = Student.Student()
    def slogin():
        name = input("请输入您的名字：")
        fddir = os.path.dirname(os.path.dirname(__file__))
        with open('%s\dumpfile\student\%s' % (fddir, name), 'rb') as fd:
            studentobj = pickle.load(fd)
        return studentobj

    studentmanageoptdic0 = {'1': studentobj.reg, '2': slogin, '3': exit}
    flag = True
    while flag:
        studentmanopt = input("你要干什么？\n1：注册\n2：登陆\n3:退出\n")
        if studentmanopt in studentmanageoptdic0.keys():
            studentobj = studentmanageoptdic0[studentmanopt]()
        if studentmanopt=='2':
            break




    studentmanageoptdic = { '1': studentobj.addgroup, '2': studentobj.scorecheck,
                           '3': studentobj.pay, '4': exit}
    flag = True
    while flag:
        studentmanopt = input("你要干什么？\n1：报名（选择要上的班级）\n2：查成绩\n3：缴费\n4:退出\n")
        if studentmanopt in studentmanageoptdic.keys():
            studentobj = studentmanageoptdic[studentmanopt]()
    return
